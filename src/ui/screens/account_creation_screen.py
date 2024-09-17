# account_creation_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from kivy.lang import Builder

class AccountCreationScreen(ColoredScreen):
    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/account_creation_view.kv')
        super().__init__(**kwargs)

    def register(self):
        new_username = self.ids.new_username_input.text
        new_password = self.ids.new_password_input.text
        confirm_password = self.ids.confirm_password_input.text

        if new_password != confirm_password:
            print("Passwords do not match!")
        else:
            print("Registration successful!")
            self.manager.current = 'menu_screen'

    def back_button(self):
        self.manager.current = 'register_screen'
    