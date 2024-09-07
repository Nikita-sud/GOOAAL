from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.backend.models import add_order

class PizzaApp(App):
    def build(self):
        return Builder.load_file('mobile_views.kv')

    def order_pizza(self):
        username = self.root.ids.username_input.text
        password = self.root.ids.password_input.text
        
        customer_id = 1
        pizza_id = 2 
        if username and password:  # Проверяем, что поля заполнены
            add_order(customer_id, pizza_id, username, password)
            print("Заказ добавлен!")
        else:
            print("Введите имя пользователя и пароль!")

if __name__ == '__main__':
    PizzaApp().run()