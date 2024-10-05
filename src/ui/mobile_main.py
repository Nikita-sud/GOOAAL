# mobile_main.py

import sys
import os
# Add the parent directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.properties import ObjectProperty

# Import custom screens
from ui.screens.login_screen import LoginScreen
from ui.screens.register_screen import RegisterScreen
from ui.screens.account_creation_screen import AccountCreationScreen
from ui.screens.basket_screen import BasketScreen
from ui.screens.menu_screen import Menu
from ui.ui_components.paginated_grid.paginated_grid import PaginatedGrid
from ui.screens.order_history_screen import OrderHistoryScreen
from ui.screens.order_details_screen import OrderDetailsScreen
from ui.screens.employee_active_order_screen import Employee_Active_order_Screen

# Import repositories and database connection
from backend.database import connect_to_db
from backend.repositories.orders.order_repo import OrderRepo
from backend.repositories.deliverymen.deliverymen_repo import DeliverymenRepo
from backend.repositories.customers.customer_repo import CustomerRepo

# Import database handlers
from utils.db_handler import download_db, upload_db, sync_db


class PizzaApp(App):
    """
    The main application class for the PizzaApp.
    Manages the application lifecycle and initializes the screen manager with all screens.
    """

    def on_start(self):
        """
        Called when the application starts.
        Synchronizes the database by importing the SQL file.
        """
        try:
            sync_db()  # Import the SQL file into the database
            print("Database synchronized successfully on start.")
        except Exception as e:
            print("DB syncing failed on start: " + str(e))

    def on_stop(self):
        """
        Called when the application is about to close.
        Uploads the current state of the database to the SQL file.
        """
        try:
            upload_db()  # Export the database to the SQL file
            print("Database uploaded successfully on stop.")
        except Exception as e:
            print("DB uploading failed on stop: " + str(e))

    def build(self):
        """
        Builds and returns the root widget of the application.
        Initializes the screen manager, connects to the database, and sets up repositories and screens.
        """
        # Set the window size and make it non-resizable
        Window.size = (400, 800)
        Window.resizable = False

        # Initialize database connection
        db_connection = connect_to_db()
        if db_connection:
            print("Database connection established.")
        else:
            print("Failed to connect to the database.")

        # Initialize repositories with the database connection
        deliverymen_repo = DeliverymenRepo(db_connection)
        customer_repo = CustomerRepo(db_connection)
        order_repo = OrderRepo(db_connection, deliverymen_repo)

        # Create the ScreenManager with a fade transition
        sm = ScreenManager(transition=FadeTransition(duration=0.1))
        sm.current_customer_id = None  # Initialize current customer ID as None

        # Add screens to the ScreenManager
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(RegisterScreen(name='register_screen'))
        sm.add_widget(OrderHistoryScreen(name='order_history_screen', order_repo=order_repo, customer_repo=customer_repo))
        sm.add_widget(OrderDetailsScreen(name='order_details_screen', order_repo=order_repo, customer_repo=customer_repo))
        sm.add_widget(Employee_Active_order_Screen(name='employee_active_order_screen'))

        # Create and add the BasketScreen, passing the order repository
        basket_screen = BasketScreen(name="basket_screen", order_repo=order_repo)
        

        # Create and add the AccountCreationScreen, passing the customer repository
        account_creation_screen = AccountCreationScreen(name='account_creation_screen', customer_repo=customer_repo)
        sm.add_widget(basket_screen)
        sm.add_widget(account_creation_screen)

        # Create and add the Menu screen, passing a reference to the BasketScreen
        menu_screen = Menu(name='menu_screen', basket_screen=basket_screen)
        sm.add_widget(menu_screen)

        # Load the initial screen (default behavior is to show the first added screen, which is LoginScreen)
        return sm


if __name__ == '__main__':
    PizzaApp().run()