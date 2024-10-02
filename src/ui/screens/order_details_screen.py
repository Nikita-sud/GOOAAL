# order_details_screen.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang import Builder
from backend.database import connect_to_db
from backend.repositories.orders.order_repo import OrderRepo
from ui.ui_components.order_item_card.order_item_card import OrderItemCard
from backend.repositories.customers.customer_repo import CustomerRepo

class OrderDetailsScreen(ColoredScreen):
    name = 'order_details_screen'
    order_id = NumericProperty(0)
    order_details = ObjectProperty(None)
    customer_details = ObjectProperty(None)

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/order_details_screen.kv')
        Builder.load_file('src/ui/ui_components/order_item_card/order_item_card.kv')
        super().__init__(**kwargs)

    def on_enter(self, *args):
        # Загружаем детали заказа
        self.load_order_details()

    def load_order_details(self):
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        customer_repo = CustomerRepo(connection)

        self.order_details = order_repo.get_order_details(self.order_id)
        customer_id = self.order_details['order']['customer_id']
        self.customer_details = customer_repo.get_customer_by_id(customer_id)

        connection.close()

        # Обновляем интерфейс
        self.update_order_details()

    def update_order_details(self):
        # Обновляем информацию о заказе
        self.ids.order_id_label.text = f"{self.order_details['order']['order_id']}"
        self.ids.order_date_label.text = f"{self.order_details['order']['created_at']}"
        self.ids.order_status_label.text = f"{self.order_details['order']['status_name']}"
        self.ids.total_price_label.text = f"{float(self.order_details['order']['total_price']):.2f}$"

        # Обновляем информацию о клиенте
        self.ids.customer_name_label.text = f"{self.customer_details['name']} {self.customer_details['last_name']}"
        self.ids.customer_address_label.text = self.customer_details['address']  # Здесь обновляем адрес

        # Обновляем список товаров
        self.ids.items_grid.clear_widgets()
        for item in self.order_details['items']:
            item_card = OrderItemCard(
                item_name=item['product_name'],
                price=float(item['price']),
                quantity=int(item['quantity'])
            )
            self.ids.items_grid.add_widget(item_card)

    def back_to_history(self):
        self.manager.current = 'order_history_screen'