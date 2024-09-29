# register_screen.py
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.screens.colored_screen import ColoredScreen
from kivy.lang import Builder
from backend.database import connect_to_db
from kivy.properties import ObjectProperty


class RegisterScreen(ColoredScreen):
    account_creation_screen = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        Builder.load_file('src/ui/screens/screens_kv/register_view.kv')
        super().__init__(**kwargs)

    def set_gender(self, gender):
        self.gender = gender

    def check_birthdate_format(self,birthdate):
        try:
            datetime.strptime(birthdate, '%d.%m.%Y')
            return True 
        except Exception:
            return False  
        
    def check_postal_code(self, input_text):
        print(input_text)
        connection = connect_to_db()
        cursor = connection.cursor()
        query = """
        SELECT street FROM postal_codes
        WHERE postal_code = %s"""
        cursor.execute(query, (input_text,))
        result = cursor.fetchone()
        if(result==None):
            self.ids.street_label.text = "We do not support this address yet :("
        else:
            self.ids.street_label.text = result[0]
        connection.close()

    def on_enter(self, *args):
        self.account_creation_screen = self.manager.get_screen('account_creation_screen')

    def continue_to_account_creation(self):
        try:
            first_name = self.ids.name_input.text
            last_name = self.ids.lastname_input.text
            birthdate = self.ids.birthdate_input.text
            gender = 1 if self.gender=="M" else 2
            street_number = self.ids.street_number_inp.text
            apart_number_input = self.ids.apart_number_input.text
            postal_code = self.ids.postal_code_input.text
            phone_number = self.ids.phone_number_input.text
            street = self.ids.street_label.text
            print(street)
            if (street != "We do not support this address yet :("):
                # create a repo for address!
                if first_name != "" and last_name != "" and birthdate != "" and gender != "" and street_number != "" and apart_number_input != "" and postal_code != "" and phone_number != "":
                    if (self.check_birthdate_format(birthdate)):
                        try:
                            self.account_creation_screen.first_name = first_name
                            self.account_creation_screen.last_name = last_name
                            self.account_creation_screen.birthdate = birthdate
                            self.account_creation_screen.gender = gender
                            self.account_creation_screen.street_number = street_number
                            self.account_creation_screen.apart_number_input = apart_number_input
                            self.account_creation_screen.postal_code = postal_code
                            self.account_creation_screen.phone_number = phone_number
                            self.account_creation_screen.street = street
                            self.manager.current = 'account_creation_screen'
                        except Exception as ex:
                            print(ex)
                            self.ids.error_label.text = "Something went wrong. Try again later"
                    else:
                        self.ids.error_label.text = "Please use correct date format!"
                else:
                    self.ids.error_label.text = "Please fill up all of the fields!"
            else:
                self.ids.error_label.text = "Please provide another postal code"
        except Exception as ex:
            print(ex)
            self.ids.error_label.text = "Please fill up all of the fields!"

