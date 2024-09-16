# register_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from kivy.lang import Builder

class RegisterScreen(ColoredScreen):

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/register_view.kv')
        super().__init__(**kwargs)
    
    def continue_to_account_creation(self):
        self.manager.current = 'account_creation_screen'