from backend.repositories.pizza.pizza_intfc import PizzaInterface
from decimal import Decimal

class PizzaRepo(PizzaInterface):
    
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_pizzas(self):
        cursor = self.db_connection.cursor()
        query = "SELECT id, name FROM pizza"
        cursor.execute(query)
        return cursor.fetchall()

    def get_pizza_ingredients(self, pizza_id: int):
        cursor = self.db_connection.cursor()
        query = """
        SELECT i.name, i.price, pi.quantity
        FROM ingredient i
        JOIN pizza_ingredient pi ON pi.ingredient_id = i.id
        WHERE pi.pizza_id = %s
        """
        cursor.execute(query, (pizza_id,))
        return cursor.fetchall()

    def get_pizza_price(self, pizza_id: int) -> float:
        ingredients = self.get_pizza_ingredients(pizza_id)
        total_ingredient_price = sum([ingredient[1] * ingredient[2] for ingredient in ingredients])  # Умножаем цену ингредиента на количество
        
        margin = 0.40
        tax = 0.09
        margin = Decimal('0.40')
        tax = Decimal('0.09')

        price_with_margin = total_ingredient_price * (1 + margin)
        final_price = price_with_margin * (1 + tax)

        return round(float(final_price), 2)