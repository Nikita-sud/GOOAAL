from abc import ABC, abstractmethod

class PizzaInterface(ABC):

    @abstractmethod
    def get_pizzas(self):
        pass

    @abstractmethod
    def get_pizza_ingredients(self, pizza_id: int):
        pass

    @abstractmethod
    def get_pizza_price(self, pizza_id: int) -> float:
        pass
