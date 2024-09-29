# product_card_mini.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

class ProductCardMini(BoxLayout):
    product_name = StringProperty("Product")
    price = NumericProperty(0.0)  # Цена за единицу товара
    quantity = NumericProperty(1)  # Начальное количество
    basket_screen = None  # Ссылка на экран корзины

    def remove_from_basket(self):
        self.basket_screen.basket_items = [item for item in self.basket_screen.basket_items if item["product_name"] != self.product_name]
        self.basket_screen.update_basket()
        print(f"{self.product_name} removed from basket!")

    def increase_quantity(self):
        self.quantity += 1
        self.update_basket_item()
        self.basket_screen.update_basket()

    def decrease_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.update_basket_item()
            self.basket_screen.update_basket()
        else:
            # Если количество становится 0, удаляем товар из корзины
            self.remove_from_basket()

    def update_basket_item(self):
        # Обновляем информацию о товаре в корзине
        for item in self.basket_screen.basket_items:
            if item["product_name"] == self.product_name:
                item["quantity"] = self.quantity
                item["total_price"] = self.price * self.quantity
                break