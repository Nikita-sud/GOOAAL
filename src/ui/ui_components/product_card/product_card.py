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
    product_name = StringProperty("Product")
    price = StringProperty("0$")
    image_source = StringProperty("product_image.png")
    basket_screen = ObjectProperty(None)
    category = StringProperty("Unknown")  # Добавлено свойство category
    item_id = NumericProperty(0)          # Добавлено свойство item_id

    def add_to_basket(self):
        existing_item = next((item for item in self.basket_screen.basket_items if item["product_name"] == self.product_name), None)
        if existing_item:
            existing_item["quantity"] += 1
            existing_item["total_price"] = existing_item["quantity"] * float(self.price.replace("$", ""))
        else:
            self.basket_screen.basket_items.append({
                "product_name": self.product_name,
                "price": self.price,
                "quantity": 1,
                "total_price": float(self.price.replace("$", "")),
                "category": self.category,
                "item_id": self.item_id
            })
        self.basket_screen.update_basket()
        print(f"{self.product_name} added to basket!")

    def show_info(self):
        # Создаем контейнер для попапа
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Контейнер для изображения
        image_layout = RelativeLayout(size_hint=(1, None), height=self.minimum_height)  # Контейнер адаптируется к высоте изображения

# Основное изображение пиццы
        pizza_image = Image(source=self.image_source, size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        image_layout.add_widget(pizza_image)

        # Проверяем, является ли пицца вегетарианской
        pizza_repo = PizzaRepo(connect_to_db())
        if self.category=="Pizza" and pizza_repo.is_vegetarian(self.item_id):
            # Если вегетарианская, добавляем иконку в угол
            vegetarian_icon = Image(source='assets/images/vegetarian_icon.png', size_hint=(None, None), size=(dp(30), dp(30)), pos_hint={'right': 1, 'down': 1})
            image_layout.add_widget(vegetarian_icon)
        
        # Прокручиваемый вид для текстовой информации
        scroll_view = ScrollView(size_hint=(1, 1))
        info_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10), spacing=dp(10))
        info_layout.bind(minimum_height=info_layout.setter('height'))

        # Добавляем текстовую информацию о продукте
        info_layout.add_widget(Label(text=f"Product: {self.product_name}", font_size=sp(16), color=(0, 0, 0, 1), size_hint_y=None, height=dp(25)))
        info_layout.add_widget(Label(text=f"Price: {self.price}", font_size=sp(16), color=(0, 0, 0, 1), size_hint_y=None, height=dp(25)))
        info_layout.add_widget(Label(text=f"Category: {self.category}", font_size=sp(16), color=(0, 0, 0, 1), size_hint_y=None, height=dp(25)))

        # Если это пицца, добавляем ингредиенты
        if self.category == "Pizza":
            ingredients = pizza_repo.get_pizza_ingredients(self.item_id)

            # Добавляем заголовок "Ingredients"
            info_layout.add_widget(Label(text="Ingredients:", font_size=sp(16), color=(0, 0, 0, 1), size_hint_y=None, height=dp(25)))

            # Добавляем список ингредиентов
            for ingredient in ingredients:
                ingredient_label = Label(
                    text=f"{ingredient[1]} - {ingredient[2]}$ (x{ingredient[3]})",
                    font_size=sp(14),
                    color=(0, 0, 0, 1),
                    size_hint_y=None,
                    height=dp(25)
                )
                info_layout.add_widget(ingredient_label)

        # Добавляем info_layout в scroll_view
        scroll_view.add_widget(info_layout)

        # Добавляем layouts в основной content
        content.add_widget(image_layout)
        content.add_widget(scroll_view)

        # Создаем и показываем попап
        popup = RoundedPopup(
            title=self.product_name,
            title_color=(0, 0, 0, 1),
            title_size=sp(25),
            content=content,
            add_to_basket_callback=self.add_to_basket,  # Передаем callback
            size_hint=(0.8, 0.6)
        )
        popup.open()

class RoundedPopup(ModalView):
    def __init__(self, title, title_color, title_size, content, add_to_basket_callback, **kwargs):
        super(RoundedPopup, self).__init__(**kwargs)
        
        # Store the callback
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

        # Corrected close button
        close_button = Button(
            size_hint=(None, None),
            size=(dp(30), dp(30)),
            background_normal='assets/images/close_icon.png',  # Используем изображение как фон кнопки
            background_down='assets/images/close_icon.png',    # Опционально, можно задать эффект нажатия
            pos_hint={'right': 1, 'top': 1},
            border=(0, 0, 0, 0)  # Убираем рамку вокруг кнопки, если она есть
        )

        # Привязываем обработчик событий к самой кнопке
        close_button.bind(on_release=self.dismiss)

        # Add button to layout
        relative_layout.add_widget(close_button)
        self.container.add_widget(relative_layout)

        # Add header with title
        title_layout = BoxLayout(size_hint_y=None, height=dp(40))

        # Add a separator line below the title
        with title_layout.canvas:
            Color(0.8, 0.4, 0.1, 1)  # Separator color
            self.separator = Line(
                points=[
                    title_layout.x + dp(10), 
                    title_layout.y,  # Теперь линия привязана к низу заголовка
                    title_layout.x + title_layout.width - dp(10), 
                    title_layout.y
                ],
                width=1.1
            )

        title_label = Label(
            text=title, 
            font_size=title_size, 
            color=title_color, 
            halign='center', 
            valign='middle'
        )
        title_label.bind(size=title_label.setter('text_size'))  # Center the text
        title_layout.add_widget(title_label)

        # Добавляем title_layout с заголовком и сепаратором в основной контейнер
        self.container.add_widget(title_layout)

        # Bind position and size to update the separator when the title layout changes
        title_layout.bind(pos=self.update_separator_position, size=self.update_separator_position)

        # Add the main content
        self.container.add_widget(content)

        # Create and add the "Add to Basket" button
        add_to_basket_button = Button(
            text='Add to basket',
            size_hint_x=0.80,
            size_hint_y=None,
            background_color=(0, 0, 0, 0),
            background_normal='',
            font_size=sp(16),
            height=dp(34),
            color=(1, 1, 1, 1),  # Set text color to white
            pos_hint={'center_x': 0.5}
        )
        add_to_basket_button.bind(on_release=self.on_add_to_basket)

        # Add custom styling to the button
        with add_to_basket_button.canvas.before:
            Color(0.8, 0.4, 0.1, 1)  # Button border color
            self.button_border = RoundedRectangle(
                pos=add_to_basket_button.pos,
                size=add_to_basket_button.size,
                radius=[17]  # Half of height for fully rounded corners
            )
        add_to_basket_button.bind(pos=self.update_button_border, size=self.update_button_border)

        self.container.add_widget(add_to_basket_button)

        # Add the container to the ModalView
        self.add_widget(self.container)

    def update_rect(self, instance, value):
        """Update the position and size of the rounded rectangle."""
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_separator_position(self, instance, value):
        """Update the position and size of the separator line."""
        self.separator.points = [
            instance.x + dp(10), 
            instance.y,  # Положение линии привязано к низу title_layout
            instance.x + instance.width - dp(10), 
            instance.y
        ]

    def on_add_to_basket(self, instance):
        """Handle the Add to Basket button press."""
        if self.add_to_basket_callback:
            self.add_to_basket_callback()
        self.dismiss()

    def update_button_border(self, instance, value):
        """Update the position and size of the button border."""
        self.button_border.pos = instance.pos
        self.button_border.size = instance.size