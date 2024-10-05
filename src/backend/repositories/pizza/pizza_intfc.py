# pizza_intfc.py

from abc import ABC, abstractmethod

# Defining an abstract base class for pizza operations
class PizzaInterface(ABC):

    # Abstract method to get all available pizzas
    @abstractmethod
    def get_pizzas(self):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get ingredients of a specific pizza by pizza ID
    @abstractmethod
    def get_pizza_ingredients(self, pizza_id: int):
        pass  # Placeholder indicating this method must be implemented in derived classes

    # Abstract method to get the price of a specific pizza by pizza ID
    @abstractmethod
    def get_pizza_price(self, pizza_id: int) -> float:
        pass  # Placeholder indicating this method must be implemented in derived classes