from abc import ABC, abstractmethod

class IngredientsInterface(ABC):

    @abstractmethod
    def get_all_ingredients(self):
        pass
    
    @abstractmethod
    def get_ingredient_by_id(self, ingredient_id: int):
        pass