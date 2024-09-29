# account_creation_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from kivy.lang import Builder
from backend.repositories.customers.customer_intfc import CustomerInterface
from backend.repositories.customers.customer_repo import CustomerRepo
from backend.database import connect_to_db

class AccountCreationScreen(ColoredScreen):
    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/account_creation_view.kv')
        super().__init__(**kwargs)
        self.first_name = ""

    def on_enter(self):
        print(self.first_name)

    def register(self):
        new_username = self.ids.new_username_input.text
        new_password = self.ids.new_password_input.text
        confirm_password = self.ids.confirm_password_input.text
        if (new_username!="" and new_password!="" and confirm_password!=""):
            if new_password != confirm_password:
                self.ids.error_label.text = "Passwords do not match!"
            else:
                connection = connect_to_db()
                customer_repo: CustomerInterface = CustomerRepo(connection)
                customer_repo.create_user(self.first_name, self.last_name, self.gender, self.birthdate, self.phone_number,self.street_number, self.apart_number_input, self.postal_code, new_username, new_password)
                # customer_repo.create_credentials(new_username, new_password)
                self.ids.error_label.text = "Registration successful!"
                self.manager.current_customer_id = customer_repo.get_customer_id(new_username)
                self.manager.current = 'menu_screen'
        else:
            self.ids.error_label.text = "Please fill up all of the forms!"

    def back_button(self):
        self.manager.current = 'register_screen'
    