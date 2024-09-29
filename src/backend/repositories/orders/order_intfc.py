# order_intfc.py
from abc import ABC, abstractmethod
from backend.models import Order

class OrderInterface(ABC):

    @abstractmethod
    def save_order(self, order: Order):
        pass

    @abstractmethod
    def get_order_by_id(self, order_id):
        pass
