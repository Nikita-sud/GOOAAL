# order_intfc.py

from abc import ABC, abstractmethod
from backend.models import Order

class OrderInterface(ABC):

    @abstractmethod
    def save_order(self, order: Order):
        pass

    @abstractmethod
    def cancel_order(self, order_id: int) -> bool:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int):
        pass

    @abstractmethod
    def get_orders_by_customer_id(self, customer_id: int):
        pass

    @abstractmethod
    def get_order_details(self, order_id: int):
        pass

    @abstractmethod
    def get_all_orders(self):
        pass