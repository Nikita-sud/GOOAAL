import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from ui.screens.login_screen import LoginScreen
from ui.screens.register_screen import RegisterScreen
from ui.screens.account_creation_screen import AccountCreationScreen
from ui.screens.menu_screen import Menu
from ui.ui_components.paginated_grid.paginated_grid import PaginatedGrid


Builder.load_file('src/ui/screens/screens_kv/login_screen.kv')
Builder.load_file('src/ui/screens/screens_kv/register_view.kv')
Builder.load_file('src/ui/screens/screens_kv/account_creation_view.kv')
Builder.load_file('src/ui/screens/screens_kv/menu_screen.kv')
Builder.load_file('/Users/nichitabulgaru/Documents/DataBases/GOOAAL/src/ui/ui_components/paginated_grid/paginated_grid.kv')
Builder.load_file('/Users/nichitabulgaru/Documents/DataBases/GOOAAL/src/ui/ui_components/product_card/product_card.kv')

class PizzaApp(App):
    def build(self):
        Window.size = (400, 800)
        Window.resizable = False
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu_screen'))
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(RegisterScreen(name='register_screen'))
        sm.add_widget(AccountCreationScreen(name='account_creation_screen'))
        return sm

if __name__ == '__main__':
    PizzaApp().run()