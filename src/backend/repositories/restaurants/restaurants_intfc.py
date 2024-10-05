# restaurants_intfc.py

from abc import ABC, abstractmethod

# Defining an abstract base class for restaurant operations
class RestaurantsInterface(ABC):

    # Abstract method to add earnings for a restaurant based on a new order
    @abstractmethod
    def add_earnings(self, new_order_price: float, customer_id: int):
        pass  # Placeholder indicating this method must be implemented in derived classes