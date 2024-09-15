from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.ui_components.product_card.product_card import ProductCard 


class PaginatedGrid(BoxLayout):
    pizza_items = ListProperty([])
    drinks_items = ListProperty([])
    desserts_items = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Инициализируйте ваши товары как словари
        self.pizza_items = [
            {"product_name": "Margherita", "price": "16$", "image_source": "assets/images/pizza_image.jpeg"},
            {"product_name": "Pepperoni", "price": "18$", "image_source": "assets/images/pizza_image.jpeg"},
            {"product_name": "Four Cheese", "price": "20$", "image_source": "assets/images/pizza_image.jpeg"},
            {"product_name": "Hawaiian", "price": "22$", "image_source": "assets/images/pizza_image.jpeg"}
        ]
        self.drinks_items = [
            {"product_name": "Coke", "price": "3$", "image_source": "assets/images/coke_image.jpeg"},
            {"product_name": "Fanta", "price": "3$", "image_source": "assets/images/fanta_image.webp"}
        ]
        self.desserts_items = [
            {"product_name": "Cheesecake", "price": "7$", "image_source": "assets/images/cheesecake.jpeg"},
            {"product_name": "Ice Cream", "price": "5$", "image_source": "assets/images/ice_cream.jpeg"}
        ]

    def on_kv_post(self, base_widget):
        self.update_pages()

    def update_grid(self, grid, items):
        grid.clear_widgets()
        for item_data in items:
            item = ProductCard(**item_data)  # Здесь мы передаем словарь, и **item_data распаковывает его
            grid.add_widget(item)

    def update_pages(self):
        self.update_grid(self.ids.pizza_grid, self.pizza_items)
        self.update_grid(self.ids.drinks_grid, self.drinks_items)
        self.update_grid(self.ids.desserts_grid, self.desserts_items)