# product_card_mini.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

class ProductCardMini(BoxLayout):
    """
    A custom widget representing an individual product in the basket.
    Displays the product's name, quantity, and total price.
    Allows users to increase or decrease the quantity of the product.
    """
    # StringProperty to hold the name of the product
    product_name = StringProperty("Product")
    # NumericProperty to hold the unit price of the product
    price = NumericProperty(0.0)  # Price per unit of the product
    # NumericProperty to hold the quantity of the product in the basket
    quantity = NumericProperty(1)  # Initial quantity
    # ObjectProperty to hold a reference to the BasketScreen
    basket_screen = None  # Reference to the basket screen

    def __init__(self, **kwargs):
        """
        Initializes the ProductCardMini widget.
        
        Args:
            **kwargs: Additional keyword arguments.
        """
        super().__init__(**kwargs)
        # Additional initialization can be added here if needed

    def remove_from_basket(self):
        """
        Removes the product from the basket.
        Updates the basket items list and refreshes the basket display.
        """
        # Filter out the current product from the basket items
        self.basket_screen.basket_items = [
            item for item in self.basket_screen.basket_items
            if item["product_name"] != self.product_name
        ]
        # Update the basket display to reflect the removal
        self.basket_screen.update_basket()
        print(f"{self.product_name} removed from basket!")

    def increase_quantity(self):
        """
        Increases the quantity of the product by one.
        Updates the basket item and refreshes the basket display.
        """
        self.quantity += 1  # Increment the quantity
        self.update_basket_item()  # Update the basket item data
        self.basket_screen.update_basket()  # Refresh the basket display

    def decrease_quantity(self):
        """
        Decreases the quantity of the product by one.
        If the quantity reaches zero, removes the product from the basket.
        Updates the basket item and refreshes the basket display.
        """
        if self.quantity > 1:
            self.quantity -= 1  # Decrement the quantity
            self.update_basket_item()  # Update the basket item data
            self.basket_screen.update_basket()  # Refresh the basket display
        else:
            # If the quantity becomes 0, remove the product from the basket
            self.remove_from_basket()

    def update_basket_item(self):
        """
        Updates the product information in the basket items list.
        Sets the new quantity and recalculates the total price for the product.
        """
        # Iterate through the basket items to find the current product
        for item in self.basket_screen.basket_items:
            if item["product_name"] == self.product_name:
                item["quantity"] = self.quantity  # Update the quantity
                item["total_price"] = self.price * self.quantity  # Recalculate the total price
                break  # Exit the loop once the product is found and updated