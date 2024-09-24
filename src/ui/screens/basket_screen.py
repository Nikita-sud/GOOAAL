import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kivy.uix.screenmanager import Screen
from ui.screens.colored_screen import ColoredScreen
from kivy.properties import ListProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from ui.ui_components.product_card_mini.product_card_mini import ProductCardMini

class BasketScreen(ColoredScreen):
    basket_items = ListProperty([])  # Список товаров в корзине
    total_price = StringProperty("0$")  # Общая цена

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/basket_screen.kv')
        Builder.load_file('src/ui/ui_components/product_card_mini/product_card_mini.kv')
        super().__init__(**kwargs)

    def update_basket(self):
        self.ids.basket_items_grid.clear_widgets()
        total = 0
        for item_data in self.basket_items:
            item = ProductCardMini(**item_data)  # Создаем мини-карточку продукта
            item.basket_screen = self  # Передаем ссылку на текущий экран корзины
            box = BoxLayout(orientation='horizontal', size_hint_y=None)  # Создаем контейнер
            box.add_widget(item)  # Добавляем карточку продукта в контейнер
            self.ids.basket_items_grid.add_widget(box)
            price = float(item_data["price"].replace("$", ""))
            total += price
        
        self.total_price = f"{total:.2f}$"

    def on_kv_post(self,base_widget):
        self.update_basket()
    
    def place_order(self):
        print("Order placed with total:", self.total_price)