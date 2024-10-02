# order_repo.py

from backend.database import connect_to_db
from backend.repositories.orders.order_intfc import OrderInterface
from backend.models import Order
import threading
import time

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
        INSERT INTO orders (customer_id, total_price, status_id, created_at, discount_applied)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (order.customer_id, order.total_price, order.status_id, order.created_at, order.discount_applied))
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
        threading.Thread(target=self.update_order_status_after_delay, args=(order.order_id, 2, 15)).start()


    def update_order_status_after_delay(self, order_id, new_status, delay_seconds):
            time.sleep(delay_seconds)
            print(f"Updating order {order_id} to status {new_status} after {delay_seconds} seconds")
            self.db_connection =connect_to_db()
            cursor = self.db_connection.cursor()
            query = "UPDATE orders SET status_id = %s WHERE order_id = %s"
            cursor.execute(query, (new_status, order_id))
            self.db_connection.commit()
            cursor.close()

            if new_status == 2:
                threading.Thread(target=self.update_order_status_after_delay, args=(order_id, 3, 15)).start()

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

        # Получаем информацию о заказе, включая customer_id
        order_query = """
        SELECT o.order_id, o.customer_id, o.total_price, o.created_at, os.status_name
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
    
    def get_all_orders(self):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """SELECT o.order_id, o.total_price, o.created_at, os.status_name
        FROM orders o 
        JOIN order_status os ON o.status_id = os.status_id
        ORDER BY o.created_at DESC"""
        cursor.execute(query)
        orders = cursor.fetchall()
        cursor.close()
        return orders