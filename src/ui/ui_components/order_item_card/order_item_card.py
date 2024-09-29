# order_item_card.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

class OrderItemCard(BoxLayout):
    item_name = StringProperty("")
    price = NumericProperty(0.0)
    quantity = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)