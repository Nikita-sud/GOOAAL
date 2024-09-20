from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class ProductCardMini(BoxLayout):
    product_name = StringProperty("Product")
    price = StringProperty("0$")

    def remove_from_basket(self):
        self.basket_screen.basket_items = [item for item in self.basket_screen.basket_items if item["product_name"] != self.product_name]

        self.basket_screen.update_basket()
        print(f"{self.product_name} removed from basket!")