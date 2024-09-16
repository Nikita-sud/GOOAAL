# menu_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from ui.ui_components.product_card.product_card import ProductCard
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class Menu(ColoredScreen):
    offers_items = ListProperty([])  # Инициализация ListProperty

    def __init__(self, **kwargs):
        self.offers_items.extend([
            {"product_name": "Margherita", "price": "16$", "image_source": "assets/images/pizza_image.jpeg"},
            {"product_name": "Pepperoni", "price": "18$", "image_source": "assets/images/pizza_image.jpeg"}
        ])
        Builder.load_file('src/ui/screens/screens_kv/menu_screen.kv')
        super().__init__(**kwargs)

    def update_offers(self, special_offer_window):
        special_offer_window.clear_widgets()

        for item_data in self.offers_items:
            item = ProductCard(**item_data)
            box = BoxLayout(orientation='vertical')
            box.add_widget(item)
            special_offer_window.add_widget(box)

    def on_kv_post(self, base_widget):
        self.update_offers(self.ids.special_offers)