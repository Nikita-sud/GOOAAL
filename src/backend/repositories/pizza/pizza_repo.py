# pizza_repo.py

from backend.repositories.pizza.pizza_intfc import PizzaInterface
from decimal import Decimal

# Defining the PizzaRepo class that implements the PizzaInterface
class PizzaRepo(PizzaInterface):
    
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Method to get all available pizzas
    def get_pizzas(self):
        cursor = self.db_connection.cursor()
        query = "SELECT id, name FROM pizza"
        cursor.execute(query)  # Execute query to get all pizzas
        return cursor.fetchall()  # Fetch all pizzas

    # Method to get ingredients of a specific pizza by pizza ID
    def get_pizza_ingredients(self, pizza_id: int):
        cursor = self.db_connection.cursor()
        query = """
        SELECT i.id, i.name, i.price, pi.quantity
        FROM ingredient i
        JOIN pizza_ingredient pi ON pi.ingredient_id = i.id
        WHERE pi.pizza_id = %s
        """
        cursor.execute(query, (pizza_id,))  # Execute query to get ingredients of the pizza
        return cursor.fetchall()  # Fetch all ingredients for the specified pizza

    # Method to get discount for a specific pizza by pizza ID
    def get_pizza_discount(self, pizza_id: int):
        cursor = self.db_connection.cursor()
        query = "SELECT discount FROM menu_pizza WHERE pizza_id = %s"
        cursor.execute(query, (pizza_id,))  # Execute query to get discount for the pizza
        result = cursor.fetchone()  # Fetch the discount value

        if result and result[0]:
            return Decimal(result[0])  # Return the discount as a Decimal value
        else:
            return Decimal('0')  # Return 0 if no discount is found

    # Method to get the price of a specific pizza by pizza ID
    def get_pizza_price(self, pizza_id: int) -> float:
        cursor = self.db_connection.cursor()
        
        # Check if price is available in menu_pizza
        query = "SELECT price FROM menu_pizza WHERE pizza_id = %s"
        cursor.execute(query, (pizza_id,))  # Execute query to get price from menu_pizza
        result = cursor.fetchone()  # Fetch the price value
        
        if result and result[0] is not None:
            # Price is available in menu_pizza
            price = Decimal(result[0])
        else:
            # Price is not available, calculate it
            ingredients = self.get_pizza_ingredients(pizza_id)  # Get the ingredients of the pizza
            
            # Calculate the total ingredient price (convert to Decimal for precision)
            total_ingredient_price = sum([Decimal(ingredient[2]) * Decimal(ingredient[3]) for ingredient in ingredients])
            
            margin = Decimal('0.40')  # 40% margin
            tax = Decimal('0.09')     # 9% tax
    
            # Calculate price with margin and tax
            price_with_margin = total_ingredient_price * (1 + margin)
            price_with_tax = price_with_margin * (1 + tax)
    
            # Get discount for the pizza
            discount = self.get_pizza_discount(pizza_id)
            final_price = price_with_tax * (1 - discount)
    
            # Round to two decimal places
            price = final_price.quantize(Decimal('0.01'))

    
            # Save the calculated price in menu_pizza
            insert_query = """
            INSERT INTO menu_pizza (pizza_id, discount, price)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            discount = VALUES(discount),
            price = VALUES(price)
            """
            cursor.execute(insert_query, (pizza_id, float(discount), float(price)))  # Insert or update the price in menu_pizza
            self.db_connection.commit()  # Commit the changes to the database
        
        return float(price)  # Return the final price as a float
    
    # Method to check if a specific pizza is vegetarian
    def is_vegetarian(self, pizza_id: int) -> bool:
        cursor = self.db_connection.cursor()
        query = "SELECT vegetarian FROM pizza WHERE id = %s"
        cursor.execute(query, (pizza_id,))  # Execute query to check if the pizza is vegetarian
        result = cursor.fetchone()  # Fetch the result
        return result[0] == 1  # Return True if vegetarian, otherwise False