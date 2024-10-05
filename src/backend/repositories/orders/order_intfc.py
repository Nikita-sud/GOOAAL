# order_intfc.py

from abc import ABC, abstractmethod
from backend.models import Order

# Defining an abstract base class for order operations
class OrderInterface(ABC):

    # Abstract method to save an order to the database
    @abstractmethod
    def save_order(self, order: Order):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to cancel an order by order ID
    @abstractmethod
    def cancel_order(self, order_id: int) -> bool:
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get an order by order ID
    @abstractmethod
    def get_order_by_id(self, order_id: int):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get all orders for a given customer by customer ID
    @abstractmethod
    def get_orders_by_customer_id(self, customer_id: int):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get detailed information about an order by order ID
    @abstractmethod
    def get_order_details(self, order_id: int):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get all orders in the system
    @abstractmethod
    def get_all_orders(self):
        pass  # Placeholder indicating this method must be implemented in derived classes