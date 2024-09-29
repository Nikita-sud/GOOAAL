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

class OrderDetailsScreen(ColoredScreen):
    name = 'order_details_screen'
    order_id = NumericProperty(0)
    order_details = ObjectProperty(None)

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
        self.order_details = order_repo.get_order_details(self.order_id)
        connection.close()

        # Обновляем интерфейс
        self.update_order_details()

    def update_order_details(self):
        # Обновляем информацию на экране
        self.ids.order_id_label.text = f"Order ID: {self.order_details['order']['order_id']}"
        self.ids.order_date_label.text = f"Order Date: {self.order_details['order']['created_at']}"
        self.ids.order_status_label.text = f"Status: {self.order_details['order']['status_name']}"
        self.ids.total_price_label.text = f"Total Price: ${float(self.order_details['order']['total_price']):.2f}"

        # Обновляем список товаров
        self.ids.items_grid.clear_widgets()
        for item in self.order_details['items']:
            item_card = OrderItemCard(
                item_name=item['product_name'],
                price=float(item['price']),  # Преобразуем Decimal в float
                quantity=int(item['quantity'])  # Убедимся, что количество — это int
            )
            self.ids.items_grid.add_widget(item_card)

    def back_to_history(self):
        self.manager.current = 'order_history_screen'