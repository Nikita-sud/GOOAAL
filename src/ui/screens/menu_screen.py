# menu_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from screens.colored_screen import ColoredScreen
from ui_components.product_card.product_card import ProductCard
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.graphics import Color
from kivy.uix.image import Image
from kivy.properties import StringProperty


class Menu(ColoredScreen):
    offers_items = ListProperty([]) 
    menu_opened = False
    darken_color_instruction = ObjectProperty(None)
    basket_screen = ObjectProperty(None)
    current_category = StringProperty('Pizza')

    def __init__(self, **kwargs):
        self.offers_items.extend([
            {"product_name": "Margherita", "price": "16$", "image_source": "assets/images/pizza_image.jpeg"},
            {"product_name": "Pepperoni", "price": "18$", "image_source": "assets/images/pizza_image.jpeg"}
        ])
        Builder.load_file('src/ui/screens/screens_kv/menu_screen.kv')
        super().__init__(**kwargs)

    def update_offers(self, special_offer_window):
        special_offer_window.clear_widgets()

        for img_path in ['code_goal10.png','pizza_and_desert.png', 'pizza_and_drink.png']:
            box = BoxLayout(orientation='vertical')
            img = Image(source="assets/images/offers/"+img_path, allow_stretch=True, keep_ratio=False)
            box.add_widget(img)
            special_offer_window.add_widget(box)

    def on_enter(self, *args):
        # Get basket_screen from ScreenManager
        self.basket_screen = self.manager.get_screen('basket_screen')
        self.ids.paginated_grid.basket_screen = self.basket_screen

        
        # Recreate ProductCards with the correct basket_screen
        self.ids.paginated_grid.update_pages()
        self.update_offers(self.ids.special_offers)
        self.ids.paginated_grid.carousel_slide_change_callback = self.on_carousel_current_slide_change

    def on_kv_post(self, base_widget):
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
        print("Carousel current slide changed")
        paginated_grid = self.ids.paginated_grid
        if current_slide is paginated_grid.drinks_slide:
            self.current_category = 'Drinks'
        elif current_slide is paginated_grid.pizza_slide:
            self.current_category = 'Pizza'
        elif current_slide is paginated_grid.desserts_slide:
            self.current_category = 'Desserts'
    
    def toggle_menu(self):
        if not self.darken_color_instruction:
            return  # Проверка, что затемняющий слой инициализирован

        if self.menu_opened:
            # Закрытие меню: скрываем боковое меню и убираем затемнение
            anim_menu = Animation(pos_hint={'x': -1}, duration=0.3)
            anim_darken = Animation(rgba=(0, 0, 0, 0), duration=0.3)  # Убираем затемнение
            self.ids.darken_widget.disabled = False  # Разрешаем клики под меню
        else:
            # Открытие меню: показываем боковое меню и затемняем экран
            anim_menu = Animation(pos_hint={'x': 0}, duration=0.3)
            anim_darken = Animation(rgba=(0, 0, 0, 0.5), duration=0.3)  # Затемняем экран
            self.ids.darken_widget.disabled = True  # Блокируем клики под меню

        # Запуск анимации
        anim_menu.start(self.ids.side_menu)
        anim_darken.start(self.darken_color_instruction)

        # Переключение состояния меню
        self.menu_opened = not self.menu_opened

    def to_basket(self):
        self.manager.current = 'basket_screen'