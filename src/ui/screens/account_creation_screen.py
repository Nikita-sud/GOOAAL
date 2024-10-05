# account_creation_screen.py

# account_creation_screen.py
import sys
import os

# Add the parent directory to the system path to allow imports from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importing necessary modules from the project
from ui.screens.colored_screen import ColoredScreen  # Base class for colored screens
from kivy.lang import Builder  # Used to load the .kv design file
from backend.repositories.customers.customer_intfc import CustomerInterface  # Interface for customer operations
from backend.repositories.customers.customer_repo import CustomerRepo  # Repository for customer data
from kivy.properties import ObjectProperty  # Property type for Kivy objects

class AccountCreationScreen(ColoredScreen):
    # Define a Kivy property to hold a reference to the customer repository
    customer_repo = ObjectProperty(None)

    def __init__(self, **kwargs):
        # Load the .kv file that contains the UI design for the account creation screen
        Builder.load_file('src/ui/screens/screens_kv/account_creation_view.kv')
        super().__init__(**kwargs)  # Call the parent class constructor
        self.first_name = ""  # Initialize the first name attribute to an empty string

    def on_enter(self):
        # This method is called when the screen is entered
        # For now, it simply prints the first name to the console
        print(self.first_name)

    def register(self):
        # Retrieve the input values from the UI
        new_username = self.ids.new_username_input.text
        new_password = self.ids.new_password_input.text
        confirm_password = self.ids.confirm_password_input.text

        # Check if all fields are filled
        if new_username != "" and new_password != "" and confirm_password != "":
            # Check if the passwords match
            if new_password != confirm_password:
                # Display an error message if passwords do not match
                self.ids.error_label.text = "Passwords do not match!"
            else:
                # Create a new user with the provided information
                self.customer_repo.create_user(
                    self.first_name,
                    self.last_name,
                    self.gender,
                    self.birthdate,
                    self.phone_number,
                    self.street_number,
                    self.apart_number_input,
                    self.postal_code,
                    new_username,
                    new_password
                )
                # Display a success message
                self.ids.error_label.text = "Registration successful!"
                # Set the current customer ID in the manager to the newly created user's ID
                self.manager.current_customer_id = self.customer_repo.get_customer_id(new_username)
                # Switch to the menu screen
                self.manager.current = 'menu_screen'
        else:
            # Display an error message if any fields are left empty
            self.ids.error_label.text = "Please fill up all of the forms!"

    def back_button(self):
        # Navigate back to the registration screen
        self.manager.current = 'register_screen'