# order_card.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty
from kivy.lang import Builder
import os

class OrderCard(BoxLayout):
    order = DictProperty({})
    order_history_screen = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)