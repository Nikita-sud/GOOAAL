# basket_screen.py
import sys
import os

from backend.repositories.customers.customer_intfc import CustomerInterface
from backend.repositories.customers.customer_repo import CustomerRepo
from backend.repositories.restaurants.restaurants_intfc import RestaurantsInterface
from backend.repositories.restaurants.restaurants_repo import RestaurantsRepo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kivy.uix.screenmanager import Screen
from ui.screens.colored_screen import ColoredScreen
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from ui.ui_components.product_card_mini.product_card_mini import ProductCardMini
from backend.repositories.orders.order_repo import OrderRepo
from backend.models import Order
from kivy.metrics import dp
from backend.database import connect_to_db
import datetime
import numpy as np

class BasketScreen(ColoredScreen):
    basket_items = ListProperty([])  # Список товаров в корзине
    total_price = NumericProperty(0.0)  # Общая цена
    birth_offer = None
    def __init__(self, **kwargs):
        self.discount = 0
        Builder.load_file('src/ui/screens/screens_kv/basket_screen.kv')
        Builder.load_file('src/ui/ui_components/product_card_mini/product_card_mini.kv')
        super().__init__(**kwargs)

    def on_enter(self):
        self.birth_offer = self.check_birthday(self.manager.current_customer_id)
        self.one_free_drink, self.one_free_pizza = ((False, False) if self.birth_offer == False else (True, True))
        self.update_basket()

    def check_offer_code(self, code_name):
        try:
            print(code_name)
            connection = connect_to_db()
            cursor = connection.cursor()
            query = """
            SELECT price FROM offers
            WHERE code = %s"""
            cursor.execute(query, (code_name.lower(),))
            result = cursor.fetchone()
            if(result==None):
                self.ids.offer_message.text = "Invalid code :("
            else:
                self.ids.offer_message.text = "Discount was applied! :)"
                self.discount = result[0]
                self.total_price = self.total_price*(1-float(self.discount))
            connection.close()
        except Exception as ex:
            print(ex)
            self.ids.offer_message.text = "Invalid code :("

    def check_birthday(self, customer_id):
        connection = connect_to_db()
        cursor = connection.cursor()
        query = """
        SELECT birthdate FROM customer
        WHERE customer_id = %s"""
        cursor.execute(query, (int(customer_id),))
        result = cursor.fetchone()
        # birth_date = datetime.strptime(result[0], '%d.%m.%Y').date()
        today = datetime.datetime.today()
        birth_date = result[0]
        print(birth_date.month)
        print(today.month)

        if(birth_date.day == today.day and birth_date.month == today.month):
            self.ids.offer_message.text = "It`s your birthday! One pizza and a drink for free! :)"
            return True
        return False


    def update_basket(self):
        self.ids.basket_items_grid.clear_widgets()
        total = 0

        try:
            self.birth_offer = self.check_birthday(self.manager.current_customer_id)
            self.one_free_drink, self.one_free_pizza = ((False, False) if self.birth_offer == False else (True, True))
        except Exception:
            pass
        for item_data in self.basket_items:
            item = ProductCardMini(
                product_name=item_data['product_name'],
                price=float(item_data['price'].replace("$", "")),
                quantity=item_data.get('quantity', 1)
            )

            item.basket_screen = self  # Передаем ссылку на экран корзины
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50))
            box.add_widget(item)
            self.ids.basket_items_grid.add_widget(box)

            if(self.one_free_pizza or self.one_free_drink):
                print('birthdate offer')
                if(self.one_free_pizza==True and item_data['category']=='Pizza'):
                    if(item_data['quantity']>1):
                        self.one_free_pizza=False
                        total += item.price * (item.quantity-1)
                        self.ids.offer_message.text = "Birthdate offer was applied! :)"
                    else:
                        self.ids.offer_message.text = "Add one more pizza to get a birthdate offer! :)"
                        total += item.price * item.quantity

                elif(self.one_free_drink==True and item_data['category']=='Drink' ):
                    if(item_data['quantity']>1):
                        self.one_free_drink=False
                        total += item.price * (item.quantity-1)
                        self.ids.offer_message.text = "Birthdate offer was applied! :)"
                    else:
                        self.ids.offer_message.text = "Add one more drink to get a birthdate offer! :)"
                        total += item.price * item.quantity

                # self.birth_offer=False
            else:
                total += item.price * item.quantity
       
        self.total_price = total

    def on_kv_post(self, base_widget):
        self.update_basket()

    def place_order(self):
        if not any(item['category'] == 'Pizza' for item in self.basket_items):
            self.ids.offer_message.text = "You have to add at least one item in your basket!"
            return

        customer_id = self.manager.current_customer_id

        # Подготовка данных заказа
        order_items = []
        for item in self.basket_items:
            order_items.append({
                'item_id': item['item_id'],
                'category': item['category'],
                'quantity': item['quantity'],
                'price': float(item['price'].replace("$", "")),
            })

        # Создаем экземпляр заказа с указанием status_id
        order = Order(
            customer_id=customer_id,
            items=order_items,
            total_price=self.total_price,
            discount_applied=self.discount,
            status_id=1,
        )

        # Сохраняем заказ в базе данных
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        order_repo.save_order(order)
        connection.close()

        restaurant_repo : RestaurantsInterface = RestaurantsRepo(connect_to_db())
        restaurant_repo.add_earnings(self.total_price, customer_id)
        customer_repo : CustomerInterface = CustomerRepo(connect_to_db())
        customer_repo.update_customer_num_of_orders(customer_id)

        print(f"Заказ оформлен! Номер заказа: {order.order_id}, Сумма: {self.total_price:.2f}$")