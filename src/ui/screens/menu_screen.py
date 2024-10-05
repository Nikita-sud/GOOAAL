# menu_screen.py

import sys
import os

# Add the parent directory to the system path to allow imports from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary modules
from screens.colored_screen import ColoredScreen  # Base class for colored screens
from ui_components.product_card.product_card import ProductCard  # UI component for product cards
from kivy.properties import ListProperty, ObjectProperty, StringProperty  # Kivy properties
from kivy.uix.boxlayout import BoxLayout  # Layout for UI elements
from kivy.lang import Builder  # Load .kv files for UI
from kivy.animation import Animation  # Used for animations
from kivy.graphics import Color  # Graphics instructions for color
from kivy.uix.image import Image  # Image widget

class Menu(ColoredScreen):
    # List of offer items for the menu
    offers_items = ListProperty([])
    menu_opened = False  # Boolean to track if the side menu is open
    darken_color_instruction = ObjectProperty(None)  # Reference to the darkening effect for the screen
    basket_screen = ObjectProperty(None)  # Reference to the basket screen
    current_category = StringProperty('Pizza')  # Track the currently selected category

    def __init__(self, **kwargs):
        # Initialize the menu with some default offer items
        self.offers_items.extend([
            {"product_name": "Margherita", "price": "16$", "image_source": "assets/images/pizza_image.jpeg"},
            {"product_name": "Pepperoni", "price": "18$", "image_source": "assets/images/pizza_image.jpeg"}
        ])
        # Load the UI from the .kv file
        Builder.load_file('src/ui/screens/screens_kv/menu_screen.kv')
        super().__init__(**kwargs)  # Call the parent class constructor

    def update_offers(self, special_offer_window):
        # Update the special offers section with new images
        special_offer_window.clear_widgets()

        for img_path in ['code_goal10.png', 'pizza_and_desert.png', 'pizza_and_drink.png']:
            box = BoxLayout(orientation='vertical')  # Create a vertical BoxLayout for each offer
            img = Image(source="assets/images/offers/" + img_path, fit_mode='contain')  # Create an Image widget
            box.add_widget(img)  # Add the image to the box
            special_offer_window.add_widget(box)  # Add the box to the special offer window

    def on_enter(self, *args):
        # Called when the screen is entered
        # Get basket_screen from ScreenManager and update UI elements
        self.basket_screen = self.manager.get_screen('basket_screen')
        self.ids.paginated_grid.basket_screen = self.basket_screen
        
        # Recreate ProductCards with the correct basket_screen
        self.ids.paginated_grid.update_pages()
        self.update_offers(self.ids.special_offers)
        self.ids.paginated_grid.carousel_slide_change_callback = self.on_carousel_current_slide_change

    def on_kv_post(self, base_widget):
        # Called after the .kv file is loaded
        # Update the special offers and retrieve the darkening effect color instruction
        self.update_offers(self.ids.special_offers)
        self.ids.paginated_grid.carousel_slide_change_callback = self.on_carousel_current_slide_change
        # Retrieve the Color instruction from the darken_widget's canvas
        instructions = self.ids.darken_widget.canvas.before.get_group('darken_group')
        for instr in instructions:
            if isinstance(instr, Color):
                self.darken_color_instruction = instr
                break
        else:
            print("Color instruction not found in darken_widget's canvas.")

    def on_carousel_current_slide_change(self, current_slide):
        # Update the current category based on the current slide in the carousel
        print("Carousel current slide changed")
        paginated_grid = self.ids.paginated_grid
        if current_slide is paginated_grid.drinks_slide:
            self.current_category = 'Drinks'
        elif current_slide is paginated_grid.pizza_slide:
            self.current_category = 'Pizza'
        elif current_slide is paginated_grid.desserts_slide:
            self.current_category = 'Desserts'
    
    def toggle_menu(self):
        # Toggle the side menu open or closed
        if not self.darken_color_instruction:
            return  # Ensure the darkening layer is initialized

        if self.menu_opened:
            # Closing the menu: hide the side menu and remove the darkening effect
            anim_menu = Animation(pos_hint={'x': -1}, duration=0.3)
            anim_darken = Animation(rgba=(0, 0, 0, 0), duration=0.3)  # Remove darkening
            self.ids.darken_widget.disabled = False  # Allow clicks under the menu
        else:
            # Opening the menu: show the side menu and darken the screen
            anim_menu = Animation(pos_hint={'x': 0}, duration=0.3)
            anim_darken = Animation(rgba=(0, 0, 0, 0.5), duration=0.3)  # Darken the screen
            self.ids.darken_widget.disabled = True  # Block clicks under the menu

        # Start the animations
        anim_menu.start(self.ids.side_menu)
        anim_darken.start(self.darken_color_instruction)

        # Toggle the menu state
        self.menu_opened = not self.menu_opened

    def to_basket(self):
        # Navigate to the basket screen
        self.manager.current = 'basket_screen'