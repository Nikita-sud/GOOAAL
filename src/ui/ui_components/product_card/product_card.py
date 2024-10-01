# product_card.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class ProductCard(BoxLayout):
    product_name = StringProperty("Product")
    price = StringProperty("0$")
    image_source = StringProperty("product_image.png")
    basket_screen = ObjectProperty(None)
    category = StringProperty("Unknown")  # Добавлено свойство category
    item_id = NumericProperty(0)          # Добавлено свойство item_id

    def add_to_basket(self):
        existing_item = next((item for item in self.basket_screen.basket_items if item["product_name"] == self.product_name), None)
        if existing_item:
            existing_item["quantity"] += 1
            existing_item["total_price"] = existing_item["quantity"] * float(self.price.replace("$", ""))
        else:
            self.basket_screen.basket_items.append({
                "product_name": self.product_name,
                "price": self.price,
                "quantity": 1,
                "total_price": float(self.price.replace("$", "")),
                "category": self.category,
                "item_id": self.item_id
            })
        self.basket_screen.update_basket()
        print(f"{self.product_name} added to basket!")

    def show_info(self):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"Product: {self.product_name}"))
        content.add_widget(Label(text=f"Price: {self.price}"))
        content.add_widget(Label(text=f"Category: {self.category}"))

        popup = Popup(
            title="Product Information",
            content=content,
            size_hint=(0.8, 0.5),
            title_align='center',  # Заголовок по центру
            background='path/to/your/custom_background.png',  # Установка фонового изображения
            title_color=[1, 0.5, 0.1, 1],  # Цвет заголовка
        )
        popup.open()