# login_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from kivy.lang import Builder

class LoginScreen(ColoredScreen):

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/login_screen.kv')
        super().__init__(**kwargs)

    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        self.manager.current = 'menu_screen'