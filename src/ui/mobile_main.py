# mobile_main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.employee_active_order_screen import Employee_Active_order_Screen
from utils.db_handler import download_db, upload_db, sync_db

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.lang import Builder
from ui.screens.login_screen import LoginScreen
from ui.screens.register_screen import RegisterScreen
from ui.screens.account_creation_screen import AccountCreationScreen
from ui.screens.basket_screen import BasketScreen
from ui.screens.menu_screen import Menu
from ui.ui_components.paginated_grid.paginated_grid import PaginatedGrid
from ui.screens.order_history_screen import OrderHistoryScreen
from ui.screens.order_details_screen import OrderDetailsScreen
from ui.screens.employee_active_order_screen import Employee_Active_order_Screen

from backend.database import connect_to_db
from backend.repositories.orders.order_repo import OrderRepo
from backend.repositories.deliverymen.deliverymen_repo import DeliverymenRepo
from backend.repositories.customers.customer_repo import CustomerRepo

from utils.db_handler import download_db, upload_db, sync_db

class PizzaApp(App):

    def on_start(self):
        # This method is called when the application starts
        try:
            sync_db()  # Import the SQL file into the database
        except Exception as e:
            print("DB syncing failed on start: " + str(e))

    def on_stop(self):
        # This method is called when the application is about to close
        try:
            upload_db()  # Export the database to the SQL file
        except Exception as e:
            print("DB uploading failed on stop: " + str(e))

    def build(self):
        Window.size = (400, 800)
        Window.resizable = False

        # Инициализация соединения с базой данных
        db_connection = connect_to_db()

        # Инициализация репозиториев
        deliverymen_repo = DeliverymenRepo(db_connection)
        customer_repo = CustomerRepo(db_connection)
        order_repo = OrderRepo(db_connection, deliverymen_repo)

        # Создание ScreenManager
        sm = ScreenManager(transition=FadeTransition(duration=0.1))
        sm.current_customer_id = None

        # Добавление экранов
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(RegisterScreen(name='register_screen'))
        sm.add_widget(OrderHistoryScreen(name='order_history_screen', order_repo=order_repo, customer_repo=customer_repo))
        sm.add_widget(OrderDetailsScreen(name='order_details_screen', order_repo=order_repo, customer_repo=customer_repo))
        sm.add_widget(Employee_Active_order_Screen(name='employee_active_order_screen'))

        # Создание остальных экранов и передача репозиториев
        basket_screen = BasketScreen(name="basket_screen", order_repo=order_repo)
        account_creation_screen = AccountCreationScreen(name='account_creation_screen', customer_repo=customer_repo)
        sm.add_widget(basket_screen)
        sm.add_widget(account_creation_screen)

        menu_screen = Menu(name='menu_screen', basket_screen=basket_screen)
        sm.add_widget(menu_screen)

        return sm

if __name__ == '__main__':
    PizzaApp().run()