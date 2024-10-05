# ingredients_intfc.py

from abc import ABC, abstractmethod

class IngredientsInterface(ABC):
    """
    Abstract base class that defines the interface for ingredient repositories.
    This interface ensures that any concrete implementation provides methods
    to retrieve all ingredients and to fetch a specific ingredient by its ID.
    """

    @abstractmethod
    def get_all_ingredients(self):
        """
        Retrieve all ingredients from the data source.

        Returns:
            list: A list of tuples containing ingredient details (id, name, price).
        """
        pass

    @abstractmethod
    def get_ingredient_by_id(self, ingredient_id: int):
        """
        Retrieve a specific ingredient by its unique identifier.

        Args:
            ingredient_id (int): The unique ID of the ingredient.

        Returns:
            tuple or None: A tuple containing the ingredient's name and price if found,
                           otherwise None.
        """
        pass