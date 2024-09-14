# colored_screen.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

class ColoredScreen(Screen):
    background_color = ListProperty([0.87, 0.42, 0.16, 1])