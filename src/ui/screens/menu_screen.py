# menu_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen

class Menu(ColoredScreen):
    def update_direction(self, target_slide_id):
        carousel = self.ids.paginated_grid.ids.product_carousel
        current_slide = carousel.current_slide

        # Определение направления
        if current_slide == self.ids.paginated_grid.ids.pizza_slide:
            if target_slide_id == 'drinks_slide':
                carousel.direction = 'left'
            elif target_slide_id == 'desserts_slide':
                carousel.direction = 'right'
        elif current_slide == self.ids.paginated_grid.ids.drinks_slide:
            if target_slide_id == 'pizza_slide':
                carousel.direction = 'left'
            elif target_slide_id == 'desserts_slide':
                carousel.direction = 'left'
        elif current_slide == self.ids.paginated_grid.ids.desserts_slide:
            if target_slide_id == 'pizza_slide':
                carousel.direction = 'right'
            elif target_slide_id == 'drinks_slide':
                carousel.direction = 'right'