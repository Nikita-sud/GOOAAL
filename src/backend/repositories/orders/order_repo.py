# order_repo.py

from backend.repositories.orders.order_intfc import OrderInterface
from src.backend.database import connect_to_db
from src.backend.models import Order

class OrderRepo(OrderInterface):
    def __init__(self):
        self.db_connection = connect_to_db()

    def save_order(self, order: Order):
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO orders (customer_id, total_price, status, created_at)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (order.customer_id, order.total_price, order.status, order.created_at))
        self.db_connection.commit()
        order.order_id = cursor.lastrowid  # Получаем ID созданного заказа

        # Сохранение элементов заказа
        for item in order.items:
            item_query = """
            INSERT INTO order_items (order_id, item_id, category, price)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(item_query, (order.order_id, item['id'], item['category'], item['price']))
        self.db_connection.commit()
        cursor.close()

    def get_order_by_id(self, order_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = "SELECT * FROM orders WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        order = cursor.fetchone()
        cursor.close()
        return order