# src/ui/screens/order_history_screen.py

import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from kivy.properties import ListProperty, NumericProperty
from kivy.lang import Builder
from backend.database import connect_to_db
from backend.repositories.orders.order_repo import OrderRepo
from ui.ui_components.order_card.order_card import OrderCard  # Обновленный импорт
from kivy.clock import Clock


class OrderHistoryScreen(ColoredScreen):
    name = 'order_history_screen'
    orders = ListProperty([])
    customer_id = NumericProperty(0)
    update_timer = None

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/order_history_screen.kv')
        Builder.load_file('src/ui/ui_components/order_card/order_card.kv')
        super().__init__(**kwargs)

    def on_enter(self, *args):
        # Получаем customer_id текущего пользователя
        self.customer_id = self.manager.current_customer_id

        self.load_orders()

    def on_leave(self, *args):
        if self.update_timer:
            Clock.unschedule(self.update_timer)
            self.update_timer = None

    def load_orders(self):
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        self.orders = order_repo.get_orders_by_customer_id(self.customer_id)
        connection.close()

        self.update_orders_list()
        self.start_timer_for_update()

    def start_timer_for_update(self):
        self.update_timer = Clock.schedule_interval(self.update_current_status_history, 5)

    def update_current_status_history(self, dt):
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        self.orders = order_repo.get_orders_by_customer_id(self.customer_id)
        connection.close()
        self.update_orders_list()

    def update_orders_list(self):
        self.ids.orders_grid.clear_widgets()
        for order in self.orders:        
            order_card = OrderCard(order=order)
            order_card.order_history_screen = self
            self.ids.orders_grid.add_widget(order_card)

    def view_order_details(self, order_id):
        # Переходим на экран деталей заказа
        order_details_screen = self.manager.get_screen('order_details_screen')
        order_details_screen.order_id = order_id
        self.manager.current = 'order_details_screen'