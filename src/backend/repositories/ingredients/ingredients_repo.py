from backend.repositories.ingredients.ingredients_intfc import IngredientsInterface

class IngredientsRepo(IngredientsInterface):
    
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_ingredients(self):
        cursor = self.db_connection.cursor()
        query = "SELECT id, name, price FROM ingredient"
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_ingredient_by_id(self, ingredient_id: int):
        cursor = self.db_connection.cursor()
        query = "SELECT name, price FROM ingredient WHERE id = %s"
        cursor.execute(query, (ingredient_id,))
        return cursor.fetchone()