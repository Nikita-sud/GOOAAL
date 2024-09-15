# account_creation_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen

class AccountCreationScreen(ColoredScreen):
    def register(self):
        new_username = self.ids.new_username_input.text
        new_password = self.ids.new_password_input.text
        confirm_password = self.ids.confirm_password_input.text

        if new_password != confirm_password:
            print("Passwords do not match!")
        else:
            print("Registration successful!")
            self.manager.current = 'menu_screen'