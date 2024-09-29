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
        SELECT i.id, i.name, i.price, pi.quantity
        FROM ingredient i
        JOIN pizza_ingredient pi ON pi.ingredient_id = i.id
        WHERE pi.pizza_id = %s
        """
        cursor.execute(query, (pizza_id,))
        return cursor.fetchall()

    def get_pizza_discount(self, pizza_id: int):
        cursor = self.db_connection.cursor()
        query = "SELECT discount FROM menu_pizza WHERE pizza_id = %s"
        cursor.execute(query, (pizza_id,))
        result = cursor.fetchone()
        if result and result[0]:
            return Decimal(result[0])
        else:
            return Decimal('0')

    def get_pizza_price(self, pizza_id: int) -> float:
        cursor = self.db_connection.cursor()
        
        # Проверяем, есть ли цена в menu_pizza
        query = "SELECT price FROM menu_pizza WHERE pizza_id = %s"
        cursor.execute(query, (pizza_id,))
        result = cursor.fetchone()
        
        if result and result[0] is not None:
            # Цена присутствует в menu_pizza
            price = Decimal(result[0])
        else:
            # Цена отсутствует, вычисляем ее
            ingredients = self.get_pizza_ingredients(pizza_id)
            
            # Приводим цену ингредиентов и количество к типу Decimal
            total_ingredient_price = sum([Decimal(ingredient[2]) * Decimal(ingredient[3]) for ingredient in ingredients])
            
            margin = Decimal('0.40')  # 40% маржа
            tax = Decimal('0.09')     # 9% налог
    
            price_with_margin = total_ingredient_price * (1 + margin)
            price_with_tax = price_with_margin * (1 + tax)
    
            # Получаем скидку
            discount = self.get_pizza_discount(pizza_id)
            final_price = price_with_tax * (1 - discount)
    
            # Округляем до двух знаков после запятой
            price = final_price.quantize(Decimal('0.01'))
    
            # Сохраняем вычисленную цену в menu_pizza
            insert_query = """
            INSERT INTO menu_pizza (pizza_id, discount, price)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE discount = VALUES(discount), price = VALUES(price)
            """
            cursor.execute(insert_query, (pizza_id, float(discount), float(price)))
            self.db_connection.commit()
        
        return float(price)