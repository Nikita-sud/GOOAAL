import sys
import os
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from ui.screens.colored_screen import ColoredScreen
from ui.ui_components.order_item_card.order_item_card import OrderItemCard

# Add the parent directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class OrderDetailsScreen(ColoredScreen):
    """
    Screen that displays the details of a specific order, including customer information and ordered items.
    """
    # Screen name identifier
    name = 'order_details_screen'
    # Property to hold the order ID
    order_id = NumericProperty(0)
    # Property to hold order details fetched from the repository
    order_details = ObjectProperty(None)
    # Property to hold customer details fetched from the repository
    customer_details = ObjectProperty(None)

    # ObjectProperty for the orders repository
    order_repo = ObjectProperty(None)
    # ObjectProperty for the customers repository
    customer_repo = ObjectProperty(None)

    def __init__(self, order_repo, customer_repo, **kwargs):
        """
        Initializes the OrderDetailsScreen with the necessary repositories.
        
        Args:
            order_repo: Repository interface for accessing order data.
            customer_repo: Repository interface for accessing customer data.
            **kwargs: Additional keyword arguments.
        """
        self.order_repo = order_repo
        self.customer_repo = customer_repo
        # Load the corresponding KV files for the screen and order item cards
        Builder.load_file('src/ui/screens/screens_kv/order_details_screen.kv')
        Builder.load_file('src/ui/ui_components/order_item_card/order_item_card.kv')
        super().__init__(**kwargs)
        # Initialize the update event attribute
        self.update_event = None

    def on_enter(self, *args):
        """
        Called when the screen is entered.
        Initiates the loading of order details and starts the periodic update.
        """
        print("Entered OrderDetailsScreen")
        self.load_order_details()
        # Schedule periodic updates every 5 seconds
        self.update_event = Clock.schedule_interval(self.load_order_details, 5)

    def on_leave(self, *args):
        """
        Called when the screen is left.
        Unschedules the update event if it's running.
        """
        if self.update_event:
            self.update_event.cancel()
            self.update_event = None
            print("Unscheduling update_event in OrderDetailsScreen")

    def load_order_details(self, dt=None):
        """
        Loads the details of the current order and updates the UI accordingly.
        """
        print(f"Loading order details for order_id: {self.order_id}")
        try:
            # Fetch order details using the order repository
            self.order_details = self.order_repo.get_order_details(self.order_id)
            print(f"Fetched order details: {self.order_details}")
            if not self.order_details:
                print(f"Order {self.order_id} not found.")
                return

            # Extract customer ID from the order details
            customer_id = self.order_details['order']['customer_id']
            # Fetch customer details using the customer repository
            self.customer_details = self.customer_repo.get_customer_by_id(customer_id)
            print(f"Fetched customer details: {self.customer_details}")

            # Get the order creation time (already a datetime object)
            order_created_at = self.order_details['order']['created_at']

            # Calculate how many seconds have passed since the order was created
            elapsed_time = (datetime.now() - order_created_at).total_seconds()

            # If less than 5 seconds have passed, show the cancel button and hide it after the remaining time
            if elapsed_time < 5:
                remaining_time = 5 - elapsed_time
                self.ids.cancel_button.opacity = 1  # Make the cancel button visible
                Clock.schedule_once(self.hide_cancel_button, remaining_time)
                print(f"Cancel button visible for {remaining_time} seconds")
            else:
                # If more than 5 seconds have passed, hide the cancel button immediately
                self.ids.cancel_button.opacity = 0
                print("Cancel button hidden")

            # Update the order details displayed in the UI
            self.update_order_details()
        except Exception as e:
            print(f"Error loading order details: {e}")
            # Optionally, notify the user about the error

    def update_order_details(self):
        """
        Updates the UI elements with the latest order and customer details.
        """
        # Update order information labels
        self.ids.order_id_label.text = f"{self.order_details['order']['order_id']}"
        self.ids.order_date_label.text = f"{self.order_details['order']['created_at']}"
        self.ids.order_status_label.text = f"{self.order_details['order']['status_name']}"
        self.ids.total_price_label.text = f"{float(self.order_details['order']['total_price']):.2f}$"

        # Update customer information labels
        self.ids.customer_name_label.text = f"{self.customer_details['name']} {self.customer_details['last_name']}"
        self.ids.customer_address_label.text = self.customer_details['address']  # Update the address

        # Clear any existing widgets in the items grid
        self.ids.items_grid.clear_widgets()
        # Iterate through each item in the order and add it to the items grid
        for item in self.order_details['items']:
            item_card = OrderItemCard(
                item_name=item['product_name'],
                price=float(item['price']),
                quantity=int(item['quantity'])
            )
            self.ids.items_grid.add_widget(item_card)
        print("UI updated with latest order details")

    def back_to_history(self):
        """
        Navigates back to the order history screen.
        """
        print("Navigating back to OrderHistoryScreen")
        self.manager.current = 'order_history_screen'

    def hide_cancel_button(self, dt):
        """
        Hides the cancel button by setting its opacity to 0.
        
        Args:
            dt: Delta time passed by the Clock scheduler.
        """
        self.ids.cancel_button.opacity = 0  # Hide the cancel button
        print("Cancel button hidden by scheduler")

    def cancel_order(self):
        """
        Attempts to cancel the current order. If successful, hides the cancel button and logs the cancellation.
        """
        print(f"Attempting to cancel order {self.order_id}")
        success = self.order_repo.cancel_order(self.order_id)
        if success:
            self.ids.cancel_button.opacity = 0  # Hide the cancel button after successful cancellation
            print(f"Order {self.order_id} was canceled.")
        else:
            # Optionally, provide feedback to the user if cancellation fails
            print(f"Failed to cancel Order {self.order_id}.")