# paginated_grid.py
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.lang import Builder
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.ui_components.product_card.product_card import ProductCard
from backend.repositories.pizza.pizza_repo import PizzaRepo
from backend.database import connect_to_db

class PaginatedGrid(BoxLayout):
    pizza_items = ListProperty([])
    drinks_items = ListProperty([])
    desserts_items = ListProperty([])
    basket_screen = ObjectProperty(None)

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/ui_components/paginated_grid/paginated_grid.kv')
        Builder.load_file('src/ui/ui_components/product_card/product_card.kv')
        super().__init__(**kwargs)

        # Загружаем данные пицц из базы данных
        self.load_pizza_items()
        
        # Статические данные для напитков и десертов
        self.drinks_items.clear()
        self.drinks_items.extend([
            {"product_name": "Coke", "price": "3$", "image_source": "assets/images/coke_image.jpeg", "category": "Drink", "item_id": 1},
            {"product_name": "Fanta", "price": "3$", "image_source": "assets/images/fanta_image.webp", "category": "Drink", "item_id": 2}
        ])

        self.desserts_items.extend([
            {"product_name": "Cheesecake", "price": "7$", "image_source": "assets/images/cheesecake.jpeg", "category": "Desert", "item_id": 1},
            {"product_name": "Ice Cream", "price": "5$", "image_source": "assets/images/ice_cream.jpeg", "category": "Desert", "item_id": 2}
        ])

    def load_pizza_items(self):
        connection = connect_to_db()  # Подключение к базе данных
        pizza_repo = PizzaRepo(connection)  # Создаем экземпляр репозитория пицц
        
        self.pizza_items.clear()  # Очищаем список пицц

        pizzas = pizza_repo.get_pizzas()  # Получаем список пицц
        for pizza_id, pizza_name in pizzas:
            pizza_price = pizza_repo.get_pizza_price(pizza_id)  # Получаем динамическую цену пиццы
            self.pizza_items.append({
                "product_name": pizza_name,
                "price": f"{pizza_price}$",
                "image_source": f"assets/images/pizza/{''.join(pizza_name.lower().split(' '))}.jpg",
                "category": "Pizza",   # Добавлено поле category
                "item_id": pizza_id    # Добавлено поле item_id
            })

        connection.close()  # Закрываем соединение с базой данных

    def update_grid(self, grid, items):
        grid.clear_widgets()
        for item_data in items:
            item = ProductCard(**item_data)
            item.basket_screen = self.basket_screen  # Передаем ссылку на корзину
            grid.add_widget(item)

    def update_pages(self):
        self.update_grid(self.ids.pizza_grid, self.pizza_items)
        self.update_grid(self.ids.drinks_grid, self.drinks_items)
        self.update_grid(self.ids.desserts_grid, self.desserts_items)

    def on_kv_post(self, base_widget):
        self.update_pages()
        self.ids.product_carousel.load_slide(self.ids.pizza_slide)