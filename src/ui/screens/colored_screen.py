# colored_screen.py

import sys
import os

# Add the parent directory to the system path to allow imports from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary Kivy modules
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

class ColoredScreen(Screen):
    # Define a property for setting the background color of the screen
    background_color = ListProperty([0.87, 0.42, 0.16, 1])