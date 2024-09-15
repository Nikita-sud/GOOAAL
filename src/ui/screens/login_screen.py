# login_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen

class LoginScreen(ColoredScreen):
    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        self.manager.current = 'menu_screen'