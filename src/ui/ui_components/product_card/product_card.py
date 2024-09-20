# product_card.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

class ProductCard(BoxLayout):
    product_name = StringProperty("Product")
    price = StringProperty("0$")
    image_source = StringProperty("product_image.png")
    basket_screen = ObjectProperty(None)

    def add_to_basket(self):
        # Проверяем, установлено ли свойство basket_screen
        if self.basket_screen:
            product_info = {
                "product_name": self.product_name,
                "price": self.price
            }
            self.basket_screen.basket_items.append(product_info)  # Добавляем товар в корзину
            self.basket_screen.update_basket()  # Обновляем корзину
            print(f"{self.product_name} added to basket!")
        else:
            print("basket_screen is None in ProductCard")