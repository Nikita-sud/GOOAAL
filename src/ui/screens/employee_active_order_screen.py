import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kivy.lang import Builder
from screens.colored_screen import ColoredScreen
from ui.ui_components.order_card.order_card import OrderCard
from backend.repositories.orders.order_repo import OrderRepo
from backend.database import connect_to_db
from kivy.properties import ListProperty, NumericProperty
from kivy.clock import Clock

class Employee_Active_order_Screen(ColoredScreen):
    name = 'employee_active_order_screen'
    orders = ListProperty([])

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/employee_active_order_screen.kv')
        # Builder.load_file('src/ui/ui_components/order_card/order_card.kv')

        super().__init__(**kwargs)

    def on_enter(self, *args):
        self.load_orders()

    def load_orders(self):
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        self.orders = order_repo.get_all_orders()
        connection.close()
        self.update_orders_list()
        self.start_timer_for_update()

    def update_current_status_history(self, dt):
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        self.orders = order_repo.get_all_orders()
        connection.close()
        self.update_orders_list()

    def start_timer_for_update(self):
        self.update_timer = Clock.schedule_interval(self.update_current_status_history, 5)

    def on_leave(self, *args):
        if self.update_timer:
            Clock.unschedule(self.update_timer)
            self.update_timer = None
        
    def update_orders_list(self):
        self.ids.orders_grid_employee.clear_widgets()
        for order in self.orders:
            order_card = OrderCard(order=order)
            order_card.employee_active_order_screen = self
            self.ids.orders_grid_employee.add_widget(order_card)

    def view_order_details(self, order_id):
        order_details_screen = self.manager.get_screen('order_details_screen')
        order_details_screen.order_id = order_id
        self.manager.current = 'order_details_screen'