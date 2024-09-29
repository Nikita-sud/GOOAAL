from abc import ABC, abstractmethod

class RestaurantsInterface(ABC):

    @abstractmethod
    def add_earnings(self, new_order_price: float, customer_id:int):
        pass
