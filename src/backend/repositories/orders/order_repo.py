# order_repo.py

from backend.repositories.orders.order_intfc import OrderInterface
from backend.models import Order

class OrderRepo(OrderInterface):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save_order(self, order: Order):
        cursor = self.db_connection.cursor()

        # Устанавливаем статус по умолчанию, если он не задан
        if not hasattr(order, 'status_id'):
            order.status_id = 1  # Например, 1 - это статус "Ожидается обработка"

        # Устанавливаем дату создания, если она не задана
        if not hasattr(order, 'created_at'):
            from datetime import datetime
            order.created_at = datetime.now()

        query = """
        INSERT INTO orders (customer_id, total_price, status_id, created_at)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (order.customer_id, order.total_price, order.status_id, order.created_at))
        self.db_connection.commit()
        order.order_id = cursor.lastrowid  # Получаем ID созданного заказа

        # Сохранение элементов заказа
        for item in order.items:
            item_query = """
            INSERT INTO order_items (order_id, item_id, category, price, quantity)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(item_query, (
                order.order_id,
                item['item_id'],
                item['category'],
                item['price'],
                item['quantity']
            ))
        self.db_connection.commit()
        cursor.close()

    def get_order_by_id(self, order_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = "SELECT * FROM orders WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        order = cursor.fetchone()
        cursor.close()
        return order
    
    def get_orders_by_customer_id(self, customer_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT o.order_id, o.total_price, o.created_at, os.status_name
        FROM orders o
        JOIN order_status os ON o.status_id = os.status_id
        WHERE o.customer_id = %s
        ORDER BY o.created_at DESC
        """
        cursor.execute(query, (customer_id,))
        orders = cursor.fetchall()
        cursor.close()
        return orders

    def get_order_details(self, order_id):
        cursor = self.db_connection.cursor(dictionary=True)

        # Получаем информацию о заказе
        order_query = """
        SELECT o.order_id, o.total_price, o.created_at, os.status_name
        FROM orders o
        JOIN order_status os ON o.status_id = os.status_id
        WHERE o.order_id = %s
        """
        cursor.execute(order_query, (order_id,))
        order = cursor.fetchone()

        # Получаем товары в заказе
        items_query = """
        SELECT oi.quantity, oi.price, oi.category,
               CASE
                   WHEN oi.category = 'Pizza' THEN p.name
                   WHEN oi.category = 'Drink' THEN d.name
                   WHEN oi.category = 'Desert' THEN ds.name
                   ELSE 'Unknown'
               END AS product_name
        FROM order_items oi
        LEFT JOIN pizza p ON oi.item_id = p.ID AND oi.category = 'Pizza'
        LEFT JOIN drinks d ON oi.item_id = d.ID AND oi.category = 'Drink'
        LEFT JOIN deserts ds ON oi.item_id = ds.ID AND oi.category = 'Desert'
        WHERE oi.order_id = %s
        """
        cursor.execute(items_query, (order_id,))
        items = cursor.fetchall()
        # После получения items
        for item in items:
            item['price'] = float(item['price'])
            item['quantity'] = int(item['quantity'])

        # Преобразуем total_price
        order['total_price'] = float(order['total_price'])
        cursor.close()
        return {'order': order, 'items': items}