# src/ui/screens/order_history_screen.py

import sys
import os
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from ui.screens.colored_screen import ColoredScreen
from backend.repositories.orders.order_repo import OrderRepo
from backend.repositories.customers.customer_repo import CustomerRepo
from ui.ui_components.order_card.order_card import OrderCard

# Add the parent directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class OrderHistoryScreen(ColoredScreen):
    """
    Screen that displays the order history for the current customer.
    """
    # Screen name identifier
    name = 'order_history_screen'
    # ListProperty to hold the list of orders
    orders = ListProperty([])
    # NumericProperty to hold the current customer's ID
    customer_id = NumericProperty(0)
    # Timer reference for periodic updates
    update_timer = None

    # ObjectProperty for the orders repository
    order_repo = ObjectProperty(None)
    # ObjectProperty for the customers repository
    customer_repo = ObjectProperty(None)

    def __init__(self, order_repo, customer_repo, **kwargs):
        """
        Initializes the OrderHistoryScreen with the necessary repositories.
        
        Args:
            order_repo: Repository interface for accessing order data.
            customer_repo: Repository interface for accessing customer data.
            **kwargs: Additional keyword arguments.
        """
        self.order_repo = order_repo
        self.customer_repo = customer_repo
        # Load the corresponding KV files for the screen and order cards
        Builder.load_file('src/ui/screens/screens_kv/order_history_screen.kv')
        Builder.load_file('src/ui/ui_components/order_card/order_card.kv')
        super().__init__(**kwargs)

    def on_enter(self, *args):
        """
        Called when the screen is entered.
        Retrieves the current customer's ID and loads their orders.
        """
        # Get the customer_id of the current user from the screen manager
        self.customer_id = self.manager.current_customer_id

        # Load the orders associated with the current customer
        self.load_orders()

    def on_leave(self, *args):
        """
        Called when the screen is left.
        Unschedules the update timer if it's running.
        """
        if self.update_timer:
            Clock.unschedule(self.update_timer)
            self.update_timer = None

    def load_orders(self):
        """
        Loads the orders for the current customer and updates the UI.
        Also starts a timer to periodically update the order statuses.
        """
        # Fetch orders for the current customer using the order repository
        self.orders = self.order_repo.get_orders_by_customer_id(self.customer_id)
        # Update the orders list displayed in the UI
        self.update_orders_list()
        # Start a timer to update order statuses every 5 seconds
        self.start_timer_for_update()

    def start_timer_for_update(self):
        """
        Starts a periodic timer to update the current status of the order history.
        """
        self.update_timer = Clock.schedule_interval(self.update_current_status_history, 5)

    def update_current_status_history(self, dt):
        """
        Updates the order statuses by fetching the latest data from the repository.
        
        Args:
            dt: Delta time passed by the Clock scheduler.
        """
        # Re-fetch orders to get the latest statuses
        self.orders = self.order_repo.get_orders_by_customer_id(self.customer_id)
        # Update the orders list displayed in the UI
        self.update_orders_list()

    def update_orders_list(self):
        """
        Updates the orders grid in the UI with the latest list of orders.
        """
        # Clear existing order widgets from the grid
        self.ids.orders_grid.clear_widgets()
        # Iterate through each order and create an OrderCard for it
        for order in self.orders:
            order_card = OrderCard(order=order)
            # Reference to this screen for potential callbacks
            order_card.order_history_screen = self
            # Add the OrderCard to the orders grid
            self.ids.orders_grid.add_widget(order_card)

    def view_order_details(self, order_id):
        """
        Navigates to the Order Details screen for the specified order ID.
        
        Args:
            order_id: The ID of the order to view details for.
        """
        # Get the OrderDetailsScreen from the screen manager
        order_details_screen = self.manager.get_screen('order_details_screen')
        # Set the order_id for the OrderDetailsScreen
        order_details_screen.order_id = order_id
        # Switch to the OrderDetailsScreen
        self.manager.current = 'order_details_screen'