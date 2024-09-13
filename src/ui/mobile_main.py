from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager 
from kivy.core.window import Window

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.backend.repositories.customers.customer_intfc import CustomerInterface
from src.backend.repositories.customers.customer_repo import CustomerRepo
from src.backend.models import add_order
from src.backend.database import connect_to_db  



class PizzaApp(App):
    username = ''
    password = ''


    def build(self):
       
        return Builder.load_file('structure/mobile_views.kv')

    def on_start(self):
        try:
            Window.size = (400, 800)
            Window.resizable = False
            self.screen_manager = self.root
        except AttributeError:
            print("Error: Could not find ScreenManager")


    def login(self):
        
        self.username = self.root.ids.username_input.text
        self.password = self.root.ids.password_input.text

        try:
            connection = connect_to_db()
            customer_repo : CustomerInterface = CustomerRepo(connection)
            customer_repo.create_user(self.username, "",1, "08.12.2004", 2, 1)
            connection.close() 
            
            self.screen_manager.current = 'order_screen'
        except Exception as e:
            print(f"Ошибка входа: {e}")
            print("Неверное имя пользователя или пароль. Пожалуйста, попробуйте снова.")

    def order_pizza(self):
        customer_id = 1
        pizza_id = 2
        
        # Используем сохранённые имя пользователя и пароль для добавления заказа
        if self.username and self.password:
            add_order(customer_id, pizza_id, self.username, self.password)
            print("Заказ добавлен!")
        else:
            print("Пожалуйста, войдите в систему!")

if __name__ == '__main__':
    PizzaApp().run()