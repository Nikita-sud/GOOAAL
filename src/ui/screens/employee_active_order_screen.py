# employee_active_order_screen.py

import sys
import os

# Add the parent directory to the system path to allow imports from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary Kivy and custom modules
from kivy.lang import Builder
from screens.colored_screen import ColoredScreen  # Base class for colored screens
from ui.ui_components.order_card.order_card import OrderCard  # Custom UI component for displaying orders
from backend.repositories.orders.order_repo import OrderRepo  # Repository for order data
from backend.database import connect_to_db  # Function for connecting to the database
from kivy.properties import ListProperty  # Property for storing list of orders
from kivy.clock import Clock  # Kivy module to schedule tasks

class Employee_Active_order_Screen(ColoredScreen):
    name = 'employee_active_order_screen'  # Screen name identifier
    orders = ListProperty([])  # Property to store list of active orders

    def __init__(self, **kwargs):
        # Load the .kv file that contains the UI design for the screen
        Builder.load_file('src/ui/screens/screens_kv/employee_active_order_screen.kv')
        # Builder.load_file('src/ui/ui_components/order_card/order_card.kv')

        super().__init__(**kwargs)  # Call the parent class constructor

    def on_enter(self, *args):
        # Load orders when the screen is entered
        self.load_orders()

    def load_orders(self):
        # Load all active orders from the repository and update the UI
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        self.orders = order_repo.get_all_orders()
        connection.close()
        self.update_orders_list()
        self.start_timer_for_update()

    def update_current_status_history(self, dt):
        # Update the list of orders periodically
        connection = connect_to_db()
        order_repo = OrderRepo(connection)
        self.orders = order_repo.get_all_orders()
        connection.close()
        self.update_orders_list()

    def start_timer_for_update(self):
        # Start a timer to update the list of orders every 5 seconds
        self.update_timer = Clock.schedule_interval(self.update_current_status_history, 5)

    def on_leave(self, *args):
        # Stop the timer when leaving the screen
        if self.update_timer:
            Clock.unschedule(self.update_timer)
            self.update_timer = None
        
    def update_orders_list(self):
        # Update the UI to display the list of orders
        self.ids.orders_grid_employee.clear_widgets()
        for order in self.orders:
            order_card = OrderCard(order=order)  # Create an order card for each order
            order_card.employee_active_order_screen = self  # Set reference to the current screen
            self.ids.orders_grid_employee.add_widget(order_card)  # Add the order card to the UI

    def view_order_details(self, order_id):
        # Navigate to the order details screen
        order_details_screen = self.manager.get_screen('order_details_screen')
        order_details_screen.order_id = order_id  # Set the order ID to be viewed
        self.manager.current = 'order_details_screen'