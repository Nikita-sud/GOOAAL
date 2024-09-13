from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import sys
import os
from kivy.clock import Clock


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.backend.repositories.customers.customer_intfc import CustomerInterface
from src.backend.repositories.customers.customer_repo import CustomerRepo
from src.backend.models import add_order
from src.backend.database import connect_to_db  




class PizzaScreenManager(ScreenManager):
    pass
class LoginScreen(Screen):
    def login(self):
        app = App.get_running_app()
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        if not username or not password:
            self.ids.error_label.text = "Username and password cannot be empty!"
            # return
        else:

            try:
                connection = connect_to_db()
                customer_repo: CustomerInterface = CustomerRepo(connection)


                customer_repo.create_user(username, "", 1, "08.12.2004", 2, 1)

                app.username = username
                app.password = password
                app.connection = connection  
                self.manager.current = 'loading_screen'
                self.manager.current = 'order_screen'
            except Exception as e:
                print(f"Ошибка входа: {e}")
                print("Неверное имя пользователя или пароль. Пожалуйста, попробуйте снова.")

    def create_account(self):
        self.manager.current = 'order_screen'


class OrderScreen(Screen):
    def order_pizza(self):
        app = App.get_running_app()
        customer_id = 1
        pizza_id = 2

        if app.username and app.password:
            add_order(customer_id, pizza_id, app.username, app.password)
            print("Заказ добавлен!")
        else:
            print("Пожалуйста, войдите в систему!")        

class LoadingScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch_to_main, 3) 

    def switch_to_main(self, screen_name):
        self.manager.current = screen_name


class PizzaApp(App):
    username = ''
    password = ''
    connection = None  

    def build(self):
        Window.size = (400, 800)
        Window.resizable = False
        return Builder.load_file('structure/mobile_views.kv')

    def on_stop(self):
        if self.connection:
            self.connection.close()

if __name__ == '__main__':
    PizzaApp().run()
