from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.backend.models import add_order
from src.backend.database import connect_to_db  # Импорт функции подключения к БД

class PizzaApp(App):
    username = ''
    password = ''

    def build(self):
        return Builder.load_file('mobile_views.kv')

    def on_start(self):
        try:
            self.screen_manager = self.root
        except AttributeError:
            print("Error: Could not find ScreenManager")

    def login(self):
        # Получаем данные из полей ввода
        self.username = self.root.ids.username_input.text
        self.password = self.root.ids.password_input.text

        # Попытка подключиться к базе данных с введёнными данными
        try:
            connection = connect_to_db(self.username, self.password)
            connection.close()  # Закрываем соединение, если оно было успешным
            print("Успешный вход!")
            # Переход на экран заказа
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