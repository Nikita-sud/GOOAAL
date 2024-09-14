from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty

class ColoredScreen(Screen):
    background_color = ListProperty([0.8157, 0.4510, 0.2549, 1])  # Цвет фона #D07341

class PizzaApp(App):
    username = ''
    password = ''

    def build(self):
        self.screen_manager = ScreenManager()
        self.root = Builder.load_file('src/ui/structure/mobile_views.kv')
        return self.root

    def on_start(self):
        try:
            self.screen_manager = self.root
        except AttributeError:
            print("Error: Could not find ScreenManager")

    def login(self):
        login_screen = self.root.get_screen('login_screen')
        self.username = login_screen.ids.username_input.text
        self.password = login_screen.ids.password_input.text

        # Для демонстрации просто выведем имя пользователя и пароль
        print(f"Username: {self.username}, Password: {self.password}")

        # Здесь вы можете добавить логику входа в систему
        if self.username == 'user' and self.password == 'pass':
            print("Login successful")
            # self.screen_manager.current = 'order_screen'  # Если у вас есть экран заказа
        else:
            print("Invalid username or password. Please try again.")

    def register(self):
        account_creation_screen = self.root.get_screen('account_creation_screen')
        new_username = account_creation_screen.ids.new_username_input.text
        new_password = account_creation_screen.ids.new_password_input.text
        confirm_password = account_creation_screen.ids.confirm_password_input.text

        print(f"New Username: {new_username}, New Password: {new_password}, Confirm Password: {confirm_password}")

        if new_password != confirm_password:
            print("Passwords do not match!")
        else:
            print("Registration successful!")
            # Здесь вы можете добавить логику регистрации
            # После успешной регистрации вы можете перенаправить пользователя на экран входа
            self.root.current = 'login_screen'

    def order_pizza(self):
        customer_id = 1
        pizza_id = 2

        # Используем сохранённые имя пользователя и пароль для добавления заказа
        if self.username and self.password:
            # add_order(customer_id, pizza_id, self.username, self.password)
            print("Order added!")
        else:
            print("Please log in!")

if __name__ == '__main__':
    PizzaApp().run()