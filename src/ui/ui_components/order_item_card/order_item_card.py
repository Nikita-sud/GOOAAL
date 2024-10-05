# order_item_card.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

class OrderItemCard(BoxLayout):
    """
    A custom widget representing an individual item within an order.
    Displays the item's name, quantity, and total price.
    """
    # StringProperty to hold the name of the item
    item_name = StringProperty("")
    # NumericProperty to hold the unit price of the item
    price = NumericProperty(0.0)
    # NumericProperty to hold the quantity of the item ordered
    quantity = NumericProperty(1)

    def __init__(self, **kwargs):
        """
        Initializes the OrderItemCard widget.
        
        Args:
            **kwargs: Additional keyword arguments.
        """
        super().__init__(**kwargs)
        # Additional initialization can be added here if needed