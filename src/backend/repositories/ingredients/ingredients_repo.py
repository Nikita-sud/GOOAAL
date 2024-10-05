# ingredients_repo.py

from backend.repositories.ingredients.ingredients_intfc import IngredientsInterface

class IngredientsRepo(IngredientsInterface):
    """
    Concrete implementation of the IngredientsInterface.
    This repository interacts with the database to perform CRUD operations
    related to ingredients.
    """

    def __init__(self, db_connection):
        """
        Initializes the IngredientsRepo with a database connection.

        Args:
            db_connection: A connection object to interact with the database.
        """
        self.db_connection = db_connection

    def get_all_ingredients(self):
        """
        Retrieve all ingredients from the database.

        Executes a SQL query to fetch all records from the 'ingredient' table,
        returning their IDs, names, and prices.

        Returns:
            list: A list of tuples, each containing (id, name, price) of an ingredient.
        """
        cursor = self.db_connection.cursor()
        query = "SELECT id, name, price FROM ingredient"
        cursor.execute(query)
        ingredients = cursor.fetchall()
        cursor.close()  # It's good practice to close the cursor after use
        return ingredients

    def get_ingredient_by_id(self, ingredient_id: int):
        """
        Retrieve a specific ingredient by its ID from the database.

        Executes a SQL query to fetch the name and price of the ingredient
        with the given ID.

        Args:
            ingredient_id (int): The unique ID of the ingredient to retrieve.

        Returns:
            tuple or None: A tuple containing (name, price) if the ingredient is found,
                           otherwise None.
        """
        cursor = self.db_connection.cursor()
        query = "SELECT name, price FROM ingredient WHERE id = %s"
        cursor.execute(query, (ingredient_id,))
        ingredient = cursor.fetchone()
        cursor.close()  # Close the cursor after fetching the result
        return ingredient