# basket_screen.py
import sys
import os
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

class BasketScreen(ColoredScreen):
    basket_items = ListProperty([])  # Список товаров в корзине
    total_price = NumericProperty(0.0)  # Общая цена

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/basket_screen.kv')
        Builder.load_file('src/ui/ui_components/product_card_mini/product_card_mini.kv')
        super().__init__(**kwargs)

    def update_basket(self):
        self.ids.basket_items_grid.clear_widgets()
        total = 0
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
            total += item.price * item.quantity

        self.total_price = total

    def on_kv_post(self, base_widget):
        self.update_basket()

    def place_order(self):
        if not any(item['category'] == 'Pizza' for item in self.basket_items):
            print("Вы должны добавить хотя бы одну пиццу в заказ.")
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
            status_id=1  # Статус "Ожидается обработка"
        )

        # Сохраняем заказ в базе данных
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        order_repo.save_order(order)
        connection.close()

        print(f"Заказ оформлен! Номер заказа: {order.order_id}, Сумма: {self.total_price:.2f}$")