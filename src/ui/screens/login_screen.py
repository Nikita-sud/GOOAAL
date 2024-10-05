# login_screen.py

import sys
import os

# Add the parent directory to the system path to allow imports from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary modules from the project
from backend.repositories.employees.employee_repo import EmployeeRepo
from ui.screens.colored_screen import ColoredScreen
from kivy.lang import Builder
from backend.database import connect_to_db
from backend.repositories.customers.customer_intfc import CustomerInterface
from backend.repositories.customers.customer_repo import CustomerRepo

class LoginScreen(ColoredScreen):
    def __init__(self, **kwargs):
        # Load the .kv file that contains the UI design for the login screen
        Builder.load_file('src/ui/screens/screens_kv/login_screen.kv')
        super().__init__(**kwargs)  # Call the parent class constructor

    def login(self):
        # Retrieve the input values from the UI
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Check if both username and password fields are filled
        if username != "" and password != "":
            # Determine if the login is for an employee or a customer
            if "@" in username:
                # Employee login
                employee_repo = EmployeeRepo(connect_to_db())
                if employee_repo.check_employee(username, password):
                    # If credentials are correct, navigate to the employee active order screen
                    self.manager.current = 'employee_active_order_screen'
                else:
                    # Display an example of correct employee credentials
                    self.ids.error_label.text = "j.doe@lagoal.pizza 12345"
            else:
                # Customer login
                try:
                    connection = connect_to_db()
                    customer_repo: CustomerInterface = CustomerRepo(connection)
                    if customer_repo.check_user(username, password):
                        # Set the current customer ID in the manager to the logged-in user's ID
                        self.manager.current_customer_id = customer_repo.get_customer_id(username)
                        # Navigate to the menu screen
                        self.manager.current = 'menu_screen'
                    else:
                        # Display an error message if the credentials are incorrect
                        self.ids.error_label.text = "Your username/password is wrong"
                except Exception as ex:
                    # Display an error message if something goes wrong during login
                    print(ex)
                    self.ids.error_label.text = "Something went wrong. Try again later"
        else:
            # Display an error message if any fields are left empty
            self.ids.error_label.text = "Please enter your login/password"