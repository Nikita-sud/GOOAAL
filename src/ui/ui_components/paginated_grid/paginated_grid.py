# paginated_grid.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.lang import Builder
import sys
import os

# Add the parent directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ui.ui_components.product_card.product_card import ProductCard
from backend.repositories.pizza.pizza_repo import PizzaRepo
from backend.database import connect_to_db
from kivy.properties import ObjectProperty


class PaginatedGrid(BoxLayout):
    """
    A custom widget that displays products in a paginated grid format using a Carousel.
    Supports categories such as Pizza, Drinks, and Desserts.
    """
    # ListProperty to hold pizza items
    pizza_items = ListProperty([])
    # ListProperty to hold drinks items
    drinks_items = ListProperty([])
    # ListProperty to hold desserts items
    desserts_items = ListProperty([])
    # ObjectProperty to reference the BasketScreen for adding items to the basket
    basket_screen = ObjectProperty(None)
    # Reference to the Carousel widget defined in the KV file
    product_carousel = ObjectProperty(None)
    # Callback function to handle carousel slide changes
    carousel_slide_change_callback = ObjectProperty(None)

    # References to each slide's BoxLayout
    drinks_slide = ObjectProperty(None)
    pizza_slide = ObjectProperty(None)
    desserts_slide = ObjectProperty(None)

    def __init__(self, **kwargs):
        """
        Initializes the PaginatedGrid widget by loading the associated KV files and populating product categories.
        
        Args:
            **kwargs: Additional keyword arguments.
        """
        # Load the corresponding KV files for the paginated grid and product cards
        Builder.load_file('src/ui/ui_components/paginated_grid/paginated_grid.kv')
        Builder.load_file('src/ui/ui_components/product_card/product_card.kv')
        super().__init__(**kwargs)

        # Load pizza items from the database
        self.load_pizza_items()
        
        # Initialize drinks items with static data
        self.drinks_items.clear()
        self.drinks_items.extend([
            {
                "product_name": "Coke",
                "price": "3$",
                "image_source": "assets/images/coke_image.jpeg",
                "category": "Drink",
                "item_id": 1
            },
            {
                "product_name": "Fanta",
                "price": "3$",
                "image_source": "assets/images/fanta_image.webp",
                "category": "Drink",
                "item_id": 2
            }
        ])

        # Initialize desserts items with static data
        self.desserts_items.extend([
            {
                "product_name": "Cheesecake",
                "price": "7$",
                "image_source": "assets/images/cheesecake.jpeg",
                "category": "Dessert",
                "item_id": 1
            },
            {
                "product_name": "Ice Cream",
                "price": "5$",
                "image_source": "assets/images/ice_cream.jpeg",
                "category": "Dessert",
                "item_id": 2
            }
        ])

    def load_pizza_items(self):
        """
        Loads pizza items from the database and populates the pizza_items list.
        """
        # Establish a connection to the database
        connection = connect_to_db()  # Connect to the database
        # Create an instance of the PizzaRepo to interact with pizza data
        pizza_repo = PizzaRepo(connection)  # Instantiate PizzaRepo
        
        # Clear any existing pizza items
        self.pizza_items.clear()  # Clear the pizza_items list

        # Fetch the list of pizzas from the repository
        pizzas = pizza_repo.get_pizzas()  # Retrieve pizzas
        for pizza_id, pizza_name in pizzas:
            # Fetch the dynamic price for each pizza
            pizza_price = pizza_repo.get_pizza_price(pizza_id)  # Get pizza price
            # Append the pizza details to the pizza_items list
            self.pizza_items.append({
                "product_name": pizza_name,
                "price": f"{pizza_price}$",
                "image_source": f"assets/images/pizza/{''.join(pizza_name.lower().split(' '))}.jpg",
                "category": "Pizza",   # Category of the product
                "item_id": pizza_id    # Unique identifier for the pizza
            })

        # Close the database connection
        connection.close()  # Close the database connection

    def update_grid(self, grid, items):
        """
        Updates a specific grid with a list of items by adding ProductCard widgets.
        
        Args:
            grid (GridLayout): The GridLayout to populate with items.
            items (list): A list of dictionaries containing item data.
        """
        # Clear existing widgets from the grid
        grid.clear_widgets()
        # Iterate through each item and create a ProductCard
        for item_data in items:
            item = ProductCard(**item_data)  # Create a ProductCard with item data
            item.basket_screen = self.basket_screen  # Assign the basket_screen reference
            grid.add_widget(item)  # Add the ProductCard to the grid

    def update_pages(self):
        """
        Updates all product category grids with the latest items.
        """
        # Update the Pizza grid with pizza items
        self.update_grid(self.ids.pizza_grid, self.pizza_items)
        # Update the Drinks grid with drinks items
        self.update_grid(self.ids.drinks_grid, self.drinks_items)
        # Update the Desserts grid with desserts items
        self.update_grid(self.ids.desserts_grid, self.desserts_items)

    def on_kv_post(self, base_widget):
        """
        Called after the KV language is fully processed.
        Populates the product grids and sets up the carousel slide change callback.
        
        Args:
            base_widget: The base widget reference.
        """
        # Populate the grids with product items
        self.update_pages()
        # Load the pizza_slide into the Carousel (initial slide)
        self.ids.product_carousel.load_slide(self.ids.pizza_slide)
        # Bind the carousel's current_slide property to handle slide changes
        self.product_carousel.bind(on_current_slide=self.on_carousel_current_slide_change)

    def on_carousel_current_slide_change(self, carousel, current_slide):
        """
        Callback function triggered when the current slide of the carousel changes.
        Executes the carousel_slide_change_callback if it's set.
        
        Args:
            carousel (Carousel): The Carousel instance.
            current_slide (Widget): The currently active slide.
        """
        if self.carousel_slide_change_callback:
            self.carousel_slide_change_callback(current_slide)