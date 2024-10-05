# register_screen.py

from datetime import datetime
import sys
import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from ui.screens.colored_screen import ColoredScreen
from backend.database import connect_to_db

# Add the parent directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class RegisterScreen(ColoredScreen):
    """
    Screen that handles user registration by collecting personal information and validating input.
    """
    # ObjectProperty to hold a reference to the Account Creation Screen
    account_creation_screen = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        """
        Initializes the RegisterScreen and loads the associated KV file.
        
        Args:
            **kwargs: Additional keyword arguments.
        """
        # Load the corresponding KV file for the register screen
        Builder.load_file('src/ui/screens/screens_kv/register_view.kv')
        super().__init__(**kwargs)

    def set_gender(self, gender):
        """
        Sets the gender of the user based on input.
        
        Args:
            gender (str): The gender selected by the user ("M" for male, "F" for female).
        """
        self.gender = gender

    def check_birthdate_format(self, birthdate):
        """
        Validates the birthdate format to ensure it matches 'dd.mm.yyyy'.
        
        Args:
            birthdate (str): The birthdate string entered by the user.
        
        Returns:
            bool: True if the format is correct, False otherwise.
        """
        try:
            datetime.strptime(birthdate, '%d.%m.%Y')
            return True 
        except Exception:
            return False  

    def check_postal_code(self, input_text):
        """
        Checks if the entered postal code is supported by querying the database.
        Updates the street label based on the result.
        
        Args:
            input_text (str): The postal code entered by the user.
        """
        print(input_text)
        connection = connect_to_db()
        cursor = connection.cursor()
        query = """
        SELECT street FROM postal_codes
        WHERE postal_code = %s"""
        cursor.execute(query, (input_text,))
        result = cursor.fetchone()
        if result is None:
            # Update the street label to indicate unsupported address
            self.ids.street_label.text = "We do not support this address yet :("
        else:
            # Display the street associated with the postal code
            self.ids.street_label.text = result[0]
        connection.close()

    def on_enter(self, *args):
        """
        Called when the screen is entered.
        Retrieves a reference to the Account Creation Screen from the screen manager.
        """
        self.account_creation_screen = self.manager.get_screen('account_creation_screen')

    def continue_to_account_creation(self):
        """
        Validates the input fields and navigates to the Account Creation Screen if all validations pass.
        Displays appropriate error messages otherwise.
        """
        try:
            # Retrieve input values from the UI
            first_name = self.ids.name_input.text
            last_name = self.ids.lastname_input.text
            birthdate = self.ids.birthdate_input.text
            gender = 1 if self.gender == "M" else 2  # 1 for Male, 2 for Female
            street_number = self.ids.street_number_inp.text
            apart_number_input = self.ids.apart_number_input.text
            postal_code = self.ids.postal_code_input.text
            phone_number = self.ids.phone_number_input.text
            street = self.ids.street_label.text
            print(street)
            
            # Check if the street is supported
            if street != "We do not support this address yet :(":
                # Ensure all fields are filled
                if all([
                    first_name, last_name, birthdate, gender,
                    street_number, apart_number_input, postal_code, phone_number
                ]):
                    # Validate the birthdate format
                    if self.check_birthdate_format(birthdate):
                        try:
                            # Pass the collected data to the Account Creation Screen
                            self.account_creation_screen.first_name = first_name
                            self.account_creation_screen.last_name = last_name
                            self.account_creation_screen.birthdate = birthdate
                            self.account_creation_screen.gender = gender
                            self.account_creation_screen.street_number = street_number
                            self.account_creation_screen.apart_number_input = apart_number_input
                            self.account_creation_screen.postal_code = postal_code
                            self.account_creation_screen.phone_number = phone_number
                            self.account_creation_screen.street = street
                            
                            # Navigate to the Account Creation Screen
                            self.manager.current = 'account_creation_screen'
                        except Exception as ex:
                            # Log the exception and display an error message
                            print(ex)
                            self.ids.error_label.text = "Something went wrong. Try again later"
                    else:
                        # Display an error message for incorrect birthdate format
                        self.ids.error_label.text = "Please use the correct date format (dd.mm.yyyy)!"
                else:
                    # Display an error message for incomplete fields
                    self.ids.error_label.text = "Please fill up all of the fields!"
            else:
                # Prompt the user to provide a different postal code
                self.ids.error_label.text = "Please provide another postal code"
        except Exception as ex:
            # Log the exception and display a generic error message
            print(ex)
            self.ids.error_label.text = "Please fill up all of the fields!"