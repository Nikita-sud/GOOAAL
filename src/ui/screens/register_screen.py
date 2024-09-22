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
        first_name = self.ids.name_input.text
        last_name = self.ids.lastname_input.text
        birthdate = self.ids.birthdate_input.text
        gender_m = self.ids.gender_m.state
        city = self.ids.city_input
        house_number = self.ids.house_number_input.text
        postal_code = self.ids.postal_code_input.text
        phone_numer = self.ids.phone_number_input.text
        print(gender_m)
        self.manager.current = 'register_screen'