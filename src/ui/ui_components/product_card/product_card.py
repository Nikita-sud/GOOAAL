# product_card.py

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp, sp
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout

from backend.repositories.pizza.pizza_repo import PizzaRepo
from backend.database import connect_to_db


class ProductCard(BoxLayout):
    """
    A custom widget representing an individual product.
    Displays the product's image, name, price, and provides options to view more information
    and add the product to the basket.
    """
    # Properties to hold product details
    product_name = StringProperty("Product")
    price = StringProperty("0$")  # Price per unit
    image_source = StringProperty("product_image.png")
    basket_screen = ObjectProperty(None)
    category = StringProperty("Unknown")  # Added property for category
    item_id = NumericProperty(0)          # Added property for item ID

    def add_to_basket(self):
        """
        Adds the product to the basket.
        If the product already exists in the basket, increments its quantity and updates the total price.
        Otherwise, adds a new entry to the basket.
        """
        # Check if the product already exists in the basket
        existing_item = next(
            (item for item in self.basket_screen.basket_items if item["product_name"] == self.product_name),
            None
        )
        if existing_item:
            # Increment the quantity and update the total price
            existing_item["quantity"] += 1
            existing_item["total_price"] = existing_item["quantity"] * float(self.price.replace("$", ""))
        else:
            # Add a new product entry to the basket
            self.basket_screen.basket_items.append({
                "product_name": self.product_name,
                "price": self.price,
                "quantity": 1,
                "total_price": float(self.price.replace("$", "")),
                "category": self.category,
                "item_id": self.item_id
            })
        # Update the basket UI to reflect changes
        self.basket_screen.update_basket()
        print(f"{self.product_name} added to basket!")

    def show_info(self):
        """
        Displays a popup with detailed information about the product.
        If the product is a pizza and is vegetarian, shows a vegetarian icon.
        """
        # Create a container for the popup content
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Container for the product image
        image_layout = RelativeLayout(size_hint=(1, None), height=self.minimum_height)  # Container adapts to image height

        # Main product image
        pizza_image = Image(source=self.image_source, size_hint=(1, 1), fit_mode='contain')
        image_layout.add_widget(pizza_image)

        # Check if the product is a vegetarian pizza
        pizza_repo = PizzaRepo(connect_to_db())
        if self.category == "Pizza" and pizza_repo.is_vegetarian(self.item_id):
            # If vegetarian, add a vegetarian icon to the corner
            vegetarian_icon = Image(
                source='assets/images/vegetarian_icon.png',
                size_hint=(None, None),
                size=(dp(30), dp(30)),
                pos_hint={'right': 1, 'down': 1}
            )
            image_layout.add_widget(vegetarian_icon)
        
        # Scrollable view for textual information
        scroll_view = ScrollView(size_hint=(1, 1))
        info_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10), spacing=dp(10))
        info_layout.bind(minimum_height=info_layout.setter('height'))

        # Add product details to the info layout
        info_layout.add_widget(Label(
            text=f"Product: {self.product_name}",
            font_size=sp(16),
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(25)
        ))
        info_layout.add_widget(Label(
            text=f"Price: {self.price}",
            font_size=sp(16),
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(25)
        ))
        info_layout.add_widget(Label(
            text=f"Category: {self.category}",
            font_size=sp(16),
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(25)
        ))

        # If the product is a pizza, display its ingredients
        if self.category == "Pizza":
            ingredients = pizza_repo.get_pizza_ingredients(self.item_id)

            # Add a header for ingredients
            info_layout.add_widget(Label(
                text="Ingredients:",
                font_size=sp(16),
                color=(0, 0, 0, 1),
                size_hint_y=None,
                height=dp(25)
            ))

            # Add each ingredient to the info layout
            for ingredient in ingredients:
                ingredient_label = Label(
                    text=f"{ingredient[1]} - {ingredient[2]}$ (x{ingredient[3]})",
                    font_size=sp(14),
                    color=(0, 0, 0, 1),
                    size_hint_y=None,
                    height=dp(25)
                )
                info_layout.add_widget(ingredient_label)

        # Add the info layout to the scroll view
        scroll_view.add_widget(info_layout)

        # Add the image layout and scroll view to the main content
        content.add_widget(image_layout)
        content.add_widget(scroll_view)

        # Create and display the popup
        popup = RoundedPopup(
            title=self.product_name,
            title_color=(0, 0, 0, 1),
            title_size=sp(25),
            content=content,
            add_to_basket_callback=self.add_to_basket,  # Pass the add_to_basket callback
            size_hint=(0.8, 0.6)
        )
        popup.open()


class RoundedPopup(ModalView):
    """
    A custom popup with rounded corners that displays detailed information about a product.
    Includes a button to add the product to the basket.
    """
    def __init__(self, title, title_color, title_size, content, add_to_basket_callback, **kwargs):
        """
        Initializes the RoundedPopup with the given parameters.
        
        Args:
            title (str): The title of the popup.
            title_color (tuple): The color of the title text.
            title_size (int): The font size of the title.
            content (Widget): The main content widget to display inside the popup.
            add_to_basket_callback (function): The callback function to add the product to the basket.
            **kwargs: Additional keyword arguments.
        """
        super(RoundedPopup, self).__init__(**kwargs)
        
        # Store the callback function
        self.add_to_basket_callback = add_to_basket_callback

        # Set ModalView properties
        self.size_hint = kwargs.get('size_hint', (0.8, 0.6))
        self.background = ''  # Remove default background
        self.background_color = (0, 0, 0, 0)  # Transparent background
        self.auto_dismiss = True  # Automatically close on outside touch

        # Create the main container with rounded corners
        self.container = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        with self.container.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = RoundedRectangle(pos=self.container.pos, size=self.container.size, radius=[20])

        # Bind position and size to update the rounded rectangle
        self.container.bind(pos=self.update_rect, size=self.update_rect)

        # Create the close button in the top-right corner
        relative_layout = RelativeLayout(size_hint_y=None, height=dp(10))

        # Close button using an image as the background
        close_button = Button(
            size_hint=(None, None),
            size=(dp(30), dp(30)),
            background_normal='assets/images/close_icon.png',  # Use an image as the button background
            background_down='assets/images/close_icon.png',    # Optional: Define pressed state image
            pos_hint={'right': 1, 'top': 1},
            border=(0, 0, 0, 0)  # Remove border around the button if any
        )

        # Bind the dismiss method to the close button's release event
        close_button.bind(on_release=self.dismiss)

        # Add the close button to the relative layout
        relative_layout.add_widget(close_button)
        self.container.add_widget(relative_layout)

        # Add the title with a separator line
        title_layout = BoxLayout(size_hint_y=None, height=dp(40))

        # Add a separator line below the title
        with title_layout.canvas:
            Color(0.8, 0.4, 0.1, 1)  # Separator color (Orange)
            self.separator = Line(
                points=[
                    title_layout.x + dp(10), 
                    title_layout.y,  # Line position anchored to the bottom of the title layout
                    title_layout.x + title_layout.width - dp(10), 
                    title_layout.y
                ],
                width=1.1
            )

        # Label for the title
        title_label = Label(
            text=title, 
            font_size=title_size, 
            color=title_color, 
            halign='center', 
            valign='middle'
        )
        title_label.bind(size=title_label.setter('text_size'))  # Center the text
        title_layout.add_widget(title_label)

        # Add the title layout to the main container
        self.container.add_widget(title_layout)

        # Bind position and size to update the separator when the title layout changes
        title_layout.bind(pos=self.update_separator_position, size=self.update_separator_position)

        # Add the main content to the container
        self.container.add_widget(content)

        # Create and add the "Add to Basket" button
        add_to_basket_button = Button(
            text='Add to basket',
            size_hint_x=0.80,
            size_hint_y=None,
            background_color=(0, 0, 0, 0),  # Transparent background
            background_normal='',
            font_size=sp(16),
            height=dp(34),
            color=(1, 1, 1, 1),  # Text color (White)
            pos_hint={'center_x': 0.5}
        )
        add_to_basket_button.bind(on_release=self.on_add_to_basket)  # Bind the add_to_basket method

        # Define the border with a rounded rectangle
        with add_to_basket_button.canvas.before:
            Color(0.8, 0.4, 0.1, 1)  # Border color (Orange)
            self.button_border = RoundedRectangle(
                pos=add_to_basket_button.pos,
                size=add_to_basket_button.size,
                radius=[17]  # Half of the button's height for fully rounded corners
            )
        add_to_basket_button.bind(pos=self.update_button_border, size=self.update_button_border)

        # Add the "Add to Basket" button to the container
        self.container.add_widget(add_to_basket_button)

        # Add the container to the ModalView
        self.add_widget(self.container)

    def update_rect(self, instance, value):
        """
        Updates the position and size of the rounded rectangle to match the container.
        
        Args:
            instance: The widget instance.
            value: The new value (unused).
        """
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_separator_position(self, instance, value):
        """
        Updates the position of the separator line when the title layout changes.
        
        Args:
            instance: The widget instance.
            value: The new value (unused).
        """
        self.separator.points = [
            instance.x + dp(10), 
            instance.y,  # Line position anchored to the bottom of the title layout
            instance.x + instance.width - dp(10), 
            instance.y
        ]

    def on_add_to_basket(self, instance):
        """
        Handles the "Add to Basket" button press.
        Calls the add_to_basket_callback and dismisses the popup.
        
        Args:
            instance: The button instance.
        """
        if self.add_to_basket_callback:
            self.add_to_basket_callback()
        self.dismiss()

    def update_button_border(self, instance, value):
        """
        Updates the position and size of the button border to match the button.
        
        Args:
            instance: The button instance.
            value: The new value (unused).
        """
        self.button_border.pos = instance.pos
        self.button_border.size = instance.size