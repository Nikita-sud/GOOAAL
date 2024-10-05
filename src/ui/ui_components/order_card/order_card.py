# order_card.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty
from kivy.lang import Builder
import os

class OrderCard(BoxLayout):
    """
    A custom widget representing an individual order in the order history.
    Displays order details such as Order ID, Total Price, and Status.
    Includes a button to view more detailed information about the order.
    """
    # DictionaryProperty to hold the order data
    order = DictProperty({})
    # ObjectProperty to hold a reference to the OrderHistoryScreen
    order_history_screen = ObjectProperty(None)

    def __init__(self, **kwargs):
        """
        Initializes the OrderCard widget.
        
        Args:
            **kwargs: Additional keyword arguments.
        """
        super().__init__(**kwargs)
        # Additional initialization can be added here if needed