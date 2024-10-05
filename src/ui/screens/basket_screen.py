# basket_screen.py

import sys
import os

from backend.repositories.customers.customer_intfc import CustomerInterface
from backend.repositories.customers.customer_repo import CustomerRepo
from backend.repositories.restaurants.restaurants_intfc import RestaurantsInterface
from backend.repositories.restaurants.restaurants_repo import RestaurantsRepo

# Add the parent directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.uix.screenmanager import Screen
from ui.screens.colored_screen import ColoredScreen
from kivy.properties import ListProperty, StringProperty, NumericProperty, ObjectProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from ui.ui_components.product_card_mini.product_card_mini import ProductCardMini
from backend.repositories.orders.order_repo import OrderRepo
from backend.models import Order
from kivy.metrics import dp, sp
from backend.database import connect_to_db
import datetime
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.modalview import ModalView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class BasketScreen(ColoredScreen):
    # List of items in the basket
    basket_items = ListProperty([])  
    # Total price of items in the basket
    total_price = NumericProperty(0.0)  
    # Flag for birthday offer
    birth_offer = None
    # Discount offer percentage
    discount_offer = 0.00
    
    # ObjectProperty for the orders repository
    order_repo = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        self.discount = 0
        # Load the corresponding KV files for the screen and product cards
        Builder.load_file('src/ui/screens/screens_kv/basket_screen.kv')
        Builder.load_file('src/ui/ui_components/product_card_mini/product_card_mini.kv')
        super().__init__(**kwargs)

    def on_enter(self):
        """
        Called when the screen is entered.
        Checks for birthday offers and updates the basket.
        """
        # Check if the current customer has a birthday offer
        self.birth_offer = self.check_birthday(self.manager.current_customer_id)
        self.one_free_drink, self.one_free_pizza = (
            (False, False) if self.birth_offer == False else (True, True)
        )
        
        # Initialize the customer repository and fetch discount offers
        customer_repo: CustomerInterface = CustomerRepo(connect_to_db())
        self.discount_offer = customer_repo.get_discount_for_next(self.manager.current_customer_id)
        print(self.discount_offer)

        # Display discount message if applicable
        if self.discount_offer >= 0.1:
            self.ids.offer_message.text = "Hooray! You have a discount 10% :)"
        else:
            self.ids.offer_message.text = ''

        # Update the basket display
        self.update_basket()

    def check_offer_code(self, code_name):
        """
        Validates the offer code and applies the discount if valid.
        """
        try:
            print(code_name)
            connection = connect_to_db()
            cursor = connection.cursor()
            query = """
            SELECT price FROM offers
            WHERE code = %s"""
            cursor.execute(query, (code_name.lower(),))
            result = cursor.fetchone()
            if result is None:
                self.ids.offer_message.text = "Invalid code :("
            else:
                self.ids.offer_message.text = "Discount was applied! :)"
                self.discount = result[0]
                self.total_price = self.total_price * (1 - float(self.discount))
            connection.close()
        except Exception as ex:
            print(ex)
            self.ids.offer_message.text = "Invalid code :("

    def check_birthday(self, customer_id):
        """
        Checks if today is the customer's birthday.
        """
        connection = connect_to_db()
        cursor = connection.cursor()
        query = """
        SELECT birthdate FROM customer
        WHERE customer_id = %s"""
        cursor.execute(query, (int(customer_id),))
        result = cursor.fetchone()
        today = datetime.datetime.today()
        birth_date = result[0]

        # Compare birthdate with today's date
        if birth_date.day == today.day and birth_date.month == today.month:
            self.ids.offer_message.text = "It's your birthday! One pizza and a drink for free! :)"
            return True
        return False

    def update_basket(self):
        """
        Updates the basket display with current items and calculates the total price.
        """
        self.ids.basket_items_grid.clear_widgets()
        total = 0
        num_of_pizza = 0
        
        epsilon = 0.00001

        try:
            # Recheck birthday offer status
            self.birth_offer = self.check_birthday(self.manager.current_customer_id)
            self.one_free_drink, self.one_free_pizza = (
                (False, False) if self.birth_offer == False else (True, True)
            )
        except Exception:
            pass

        # Iterate through each item in the basket
        for item_data in self.basket_items:
            item = ProductCardMini(
                product_name=item_data['product_name'],
                price=float(item_data['price'].replace("$", "")),
                quantity=item_data.get('quantity', 1)
            )

            item.basket_screen = self  
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50))
            box.add_widget(item)
            self.ids.basket_items_grid.add_widget(box)

            # Apply birthday offers if applicable
            if self.one_free_pizza or self.one_free_drink:
                print('birthday offer')
                if self.one_free_pizza and item_data['category'] == 'Pizza':
                    if item_data['quantity'] > 1:
                        self.one_free_pizza = False
                        total += item.price * (item.quantity - 1)
                        self.ids.offer_message.text = "Birthday offer was applied! :)"
                    else:
                        self.ids.offer_message.text = "Add one more pizza to get a birthday offer! :)"
                        total += item.price * item.quantity

                elif self.one_free_drink and item_data['category'] == 'Drink':
                    if item_data['quantity'] > 1:
                        self.one_free_drink = False
                        total += item.price * (item.quantity - 1)
                        self.ids.offer_message.text = "Birthday offer was applied! :)"
                    else:
                        self.ids.offer_message.text = "Add one more drink to get a birthday offer! :)"
                        total += item.price * item.quantity
            else:
                # Regular pricing
                total += item.price * item.quantity

            # Count the number of pizzas for additional offers
            if item_data['category'] == 'Pizza':
                num_of_pizza += item_data['quantity']

        # Check for additional pizza-based offers
        if num_of_pizza >= 10:
            self.ids.offer_message.text = "If your order has more than 10 pizzas, you will receive a 10% bonus for your next order!"

        # Apply any discount offers to the total price
        self.total_price = total * (1 - self.discount_offer)

    def on_kv_post(self, base_widget):
        """
        Called after the KV language is applied.
        """
        self.update_basket()

    def show_order_popup(self):
        """
        Displays a popup with the order details and total price.
        """
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Create a scrollable view for the order items
        scroll_view = ScrollView(size_hint=(1, 1))
        order_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10), spacing=dp(10))
        order_layout.bind(minimum_height=order_layout.setter('height'))

        # Add a header label
        order_layout.add_widget(Label(text="Your Order:", font_size=sp(18), color=(0, 0, 0, 1), size_hint_y=None, height=dp(30)))

        # Add each item in the basket to the popup
        for item in self.basket_items:
            tot_price = item['quantity'] * float(item['price'].replace("$", ''))
            order_item_label = Label(
                text=f"{item['quantity']}x {item['product_name']} - ${tot_price}",
                font_size=sp(16),
                color=(0, 0, 0, 1),  
                size_hint_y=None,
                height=dp(30)
            )
            order_layout.add_widget(order_item_label)

        scroll_view.add_widget(order_layout)
        content.add_widget(scroll_view)

        # Add total price label
        total_price_label = Label(
            text=f"Total Price: ${self.total_price:.2f}",
            font_size=sp(18),
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(30)
        )
        content.add_widget(total_price_label)

        # Create and open the popup
        popup = RoundedPopupWithOrders(
            title="Thank you!",
            title_color=(0, 0, 0, 1),
            title_size=sp(25),
            content=content,
            orders_callback=self.view_orders,
            size_hint=(0.8, 0.6)
        )
        popup.open()

    def view_orders(self):
        """
        Navigates to the order history screen.
        """
        self.manager.current = 'order_history_screen'

    def place_order(self):
        """
        Processes the placement of an order.
        """
        # Ensure at least one pizza is in the basket
        if not any(item['category'] == 'Pizza' for item in self.basket_items):
            self.ids.offer_message.text = "You have to add at least one pizza to your basket!"
            return

        customer_id = self.manager.current_customer_id

        # Fetch the customer's address ID from the database
        connection = connect_to_db()
        cursor = connection.cursor()
        query = """
        SELECT address FROM customer WHERE customer_id = %s
        """
        cursor.execute(query, (customer_id,))
        customer_address_result = cursor.fetchone()
        customer_address_id = customer_address_result[0] if customer_address_result else None
        connection.close()

        if customer_address_id is None:
            self.ids.offer_message.text = "Address not found for customer!"
            return

        # Fetch the customer's postal code ID from the database
        connection = connect_to_db()
        cursor = connection.cursor()
        query = """
        SELECT postal_code_id FROM customer_address WHERE customer_address_id = %s
        """
        cursor.execute(query, (customer_address_id,))
        postal_code_result = cursor.fetchone()
        postal_code_id = postal_code_result[0] if postal_code_result else None
        connection.close()

        if postal_code_id is None:
            self.ids.offer_message.text = "Postal code not found for customer!"
            return

        # Prepare order items for the order model
        order_items = []
        num_of_pizza = 0
        for item in self.basket_items:
            if item['category'] == 'Pizza':
                num_of_pizza += item['quantity']
            order_items.append({
                'item_id': item['item_id'],
                'category': item['category'],
                'quantity': item['quantity'],
                'price': float(item['price'].replace("$", "")),
            })

        # Create an Order object
        order = Order(
            customer_id=customer_id,
            items=order_items,
            total_price=self.total_price,
            discount_applied=self.discount,
            status_id=1,  # Assuming '1' represents a new order status
        )
        self.ids.basket_items_grid.clear_widgets()

        # Save the order to the repository
        self.order_repo.save_order(order)

        try:
            # Assign the order to an available delivery person based on postal code
            delivery_person = self.order_repo.deliverymen_repo.find_available_delivery_person(postal_code_id)
            if delivery_person:
                self.order_repo.assign_order_to_delivery_person(order.order_id, delivery_person['employee_id'])
        except Exception as ex:
            print(f"Error while assigning delivery person: {ex}")
            # Optionally, handle the exception further or notify the user

        # Update restaurant earnings and customer order count
        restaurant_repo: RestaurantsInterface = RestaurantsRepo(connect_to_db())
        restaurant_repo.add_earnings(self.total_price, customer_id)
        customer_repo: CustomerInterface = CustomerRepo(connect_to_db())
        customer_repo.update_customer_num_of_orders(customer_id)
        
        # Reset any discount offers if applied
        if self.discount_offer > 0.00:
            customer_repo.set_discount_for_next(customer_id, 0.0)
        
        # Apply a new discount offer if the customer ordered more than 10 pizzas
        if num_of_pizza >= 10:
            customer_repo.set_discount_for_next(customer_id, 0.1)
        
        # Show the order confirmation popup
        self.show_order_popup()

        # Clear the basket and reset total price
        self.basket_items.clear()  
        self.total_price = 0.0     
        return

class RoundedPopupWithOrders(ModalView):
    """
    A custom popup with rounded corners that displays order details.
    """
    def __init__(self, title, title_color, title_size, content, orders_callback, **kwargs):
        super(RoundedPopupWithOrders, self).__init__(**kwargs)
        
        self.orders_callback = orders_callback

        self.size_hint = kwargs.get('size_hint', (0.8, 0.6))
        self.background = ''  
        self.background_color = (0, 0, 0, 0) 
        self.auto_dismiss = True 

        # Container for the popup content
        self.container = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Add a white rounded rectangle background
        with self.container.canvas.before:
            Color(1, 1, 1, 1)  
            self.rect = RoundedRectangle(pos=self.container.pos, size=self.container.size, radius=[20])

        self.container.bind(pos=self.update_rect, size=self.update_rect)

        # Add a relative layout for spacing
        relative_layout = RelativeLayout(size_hint_y=None, height=dp(10))
        self.container.add_widget(relative_layout)

        # Title layout with a separator line
        title_layout = BoxLayout(size_hint_y=None, height=dp(40))

        with title_layout.canvas:
            Color(0.8, 0.4, 0.1, 1)  # Orange color for the separator
            self.separator = Line(
                points=[
                    title_layout.x + dp(10), 
                    title_layout.y,  
                    title_layout.x + title_layout.width - dp(10), 
                    title_layout.y
                ],
                width=1.1
            )

        # Title label
        title_label = Label(
            text=title, 
            font_size=title_size, 
            color=title_color, 
            halign='center', 
            valign='middle'
        )
        title_label.bind(size=title_label.setter('text_size'))  # Ensure text is centered
        title_layout.add_widget(title_label)
        self.container.add_widget(title_layout)

        # Bind the separator to update its position when the title layout changes
        title_layout.bind(pos=self.update_separator_position, size=self.update_separator_position)

        # Add the main content to the popup
        self.container.add_widget(content)

        # "My Orders" button to navigate to the order history
        my_orders_button = Button(
            text='My Orders',
            size_hint_x=0.80,
            size_hint_y=None,
            background_color=(0, 0, 0, 0),
            background_normal='',
            font_size=sp(16),
            height=dp(34),
            color=(1, 1, 1, 1),  # White text color
            pos_hint={'center_x': 0.5}
        )
        my_orders_button.bind(on_release=self.on_my_orders)

        # Add a rounded rectangle border to the button
        with my_orders_button.canvas.before:
            Color(0.8, 0.4, 0.1, 1)  # Matching the separator color
            self.button_border = RoundedRectangle(
                pos=my_orders_button.pos,
                size=my_orders_button.size,
                radius=[17]  # Rounded corners
            )
        my_orders_button.bind(pos=self.update_button_border, size=self.update_button_border)

        self.container.add_widget(my_orders_button)

        # Add the container to the popup
        self.add_widget(self.container)

    def update_rect(self, instance, value):
        """
        Updates the position and size of the background rectangle.
        """
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_separator_position(self, instance, value):
        """
        Updates the position of the separator line in the title layout.
        """
        self.separator.points = [
            instance.x + dp(10), 
            instance.y,  
            instance.x + instance.width - dp(10), 
            instance.y
        ]

    def on_my_orders(self, instance):
        """
        Callback for the "My Orders" button to navigate to the order history.
        """
        if self.orders_callback:
            self.orders_callback()  
        self.dismiss()

    def update_button_border(self, instance, value):
        """
        Updates the position and size of the button border to match the button.
        """
        self.button_border.pos = instance.pos
        self.button_border.size = instance.size