# login_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from kivy.lang import Builder
from backend.database import connect_to_db
from backend.repositories.customers.customer_intfc import CustomerInterface
from backend.repositories.customers.customer_repo import CustomerRepo

class LoginScreen(ColoredScreen):

    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/login_screen.kv')
        super().__init__(**kwargs)

    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        if ((username != "") and (password != "")):
            try:
                connection = connect_to_db()
                customer_repo: CustomerInterface = CustomerRepo(connection)
                # customer_repo.create_user("Timur", "Jercak", 1, "12.12.2012", "+12345", 1)
                # customer_repo.create_credentials("test", "12345")
                if(customer_repo.check_user(username, password)):
                    self.manager.current = 'menu_screen' 
                else:
                    self.ids.error_label.text = "Your username/password is wrong"
            except Exception as ex:
               print(ex)
               self.ids.error_label.text = "Something went wrong. Try again later"
        else:
            self.ids.error_label.text = "Please enter your login/password"
