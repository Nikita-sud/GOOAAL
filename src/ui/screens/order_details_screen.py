# src/ui/screens/order_details_screen.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kivy.app import App
from kivy.lang import Builder
from ui.screens.colored_screen import ColoredScreen
from kivy.properties import NumericProperty, ObjectProperty
from ui.ui_components.order_item_card.order_item_card import OrderItemCard
from datetime import datetime, timedelta
from kivy.clock import Clock

class OrderDetailsScreen(ColoredScreen):
    name = 'order_details_screen'
    order_id = NumericProperty(0)
    order_details = ObjectProperty(None)
    customer_details = ObjectProperty(None)

    # Добавляем ObjectProperty для репозиториев
    order_repo = ObjectProperty(None)
    customer_repo = ObjectProperty(None)

    def __init__(self, order_repo, customer_repo, **kwargs):
        self.order_repo = order_repo
        self.customer_repo = customer_repo
        Builder.load_file('src/ui/screens/screens_kv/order_details_screen.kv')
        Builder.load_file('src/ui/ui_components/order_item_card/order_item_card.kv')
        super().__init__(**kwargs)

    def on_enter(self, *args):
        # Загружаем детали заказа
        self.load_order_details()

    def load_order_details(self):
        # Загружаем детали заказа
        self.order_details = self.order_repo.get_order_details(self.order_id)
        customer_id = self.order_details['order']['customer_id']
        self.customer_details = self.customer_repo.get_customer_by_id(customer_id)

        # Получаем время создания заказа (так как это уже объект datetime, strptime не нужен)
        order_created_at = self.order_details['order']['created_at']

        # Вычисляем, сколько секунд прошло с момента создания заказа
        elapsed_time = (datetime.now() - order_created_at).total_seconds()

        # Если прошло менее 5 секунд, показываем кнопку и прячем её через оставшееся время
        if elapsed_time < 5:
            remaining_time = 5 - elapsed_time
            self.ids.cancel_button.opacity = 1
            Clock.schedule_once(self.hide_cancel_button, remaining_time)
        else:
            # Если прошло больше 5 секунд, сразу скрываем кнопку
            self.ids.cancel_button.opacity = 0

        # Обновляем интерфейс заказа
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

    def hide_cancel_button(self, dt):
        self.ids.cancel_button.opacity = 0  # Прячем кнопку

    def cancel_order(self):
        success = self.order_repo.cancel_order(self.order_id)
        if success:
            self.ids.cancel_button.opacity = 0  # Скрываем кнопку после успешной отмены
            print(f"Order {self.order_id} was canceled.")