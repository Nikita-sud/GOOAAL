# product_card.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class ProductCard(BoxLayout):
    product_name = StringProperty("Product")
    price = StringProperty("0$")
    image_source = StringProperty("product_image.png")

    def add_to_basket(self):
        print(f"{self.product_name} added to basket!")