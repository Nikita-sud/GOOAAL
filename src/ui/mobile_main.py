import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_handler import download_db, upload_db

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from ui.screens.login_screen import LoginScreen
from ui.screens.register_screen import RegisterScreen
from ui.screens.account_creation_screen import AccountCreationScreen
from ui.screens.menu_screen import Menu
from ui.ui_components.paginated_grid.paginated_grid import PaginatedGrid


class PizzaApp(App):

    # we download the latest version of the sql file on openning
    def on_request_open(self):
        try:
            download_db()
        except Exception as e:
            print("DB downloading failed: "+str(e))
        return

    def build(self):
        # self.on_request_open()
        Window.size = (400, 800)
        Window.resizable = False
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(RegisterScreen(name='register_screen'))
        sm.add_widget(AccountCreationScreen(name='account_creation_screen'))
        sm.add_widget(Menu(name='menu_screen'))
        # Window.bind(on_request_close=self.on_request_close)
        return sm
    

    # we update sql file on closing the app
    def on_request_close(self, *args):
        try:
            upload_db()
        except Exception as e:
            print("DB uploading failed: "+str(e))
        self.stop()
        sys.exit()
        return


if __name__ == '__main__':
    PizzaApp().run()