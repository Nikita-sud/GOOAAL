# register_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen

class RegisterScreen(ColoredScreen):
    def continue_to_account_creation(self):
        # Add your logic here
        self.manager.current = 'account_creation_screen'