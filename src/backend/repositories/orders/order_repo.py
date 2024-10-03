# order_repo.py

from backend.database import connect_to_db
from backend.repositories.orders.order_intfc import OrderInterface
from backend.models import Order
import threading
import time
from datetime import datetime

class OrderRepo(OrderInterface):
    def __init__(self, db_connection, deliverymen_repo):
        self.db_connection = db_connection
        self.deliverymen_repo = deliverymen_repo  # Репозиторий для управления доставщиками

    def save_order(self, order: Order):
        cursor = self.db_connection.cursor()

        # Устанавливаем статус по умолчанию, если он не задан
        if not hasattr(order, 'status_id'):
            order.status_id = 1  # Например, 1 - это статус "Being Prepared"

        # Устанавливаем дату создания, если она не задана
        if not hasattr(order, 'created_at'):
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

        # Запуск потока для обновления статуса заказа
        threading.Thread(target=self.update_order_status_after_delay, args=(order.order_id, 2, 5)).start()

    def update_order_status_after_delay(self, order_id, new_status, delay_seconds):
        time.sleep(delay_seconds)
        print(f"Updating order {order_id} to status {new_status} after {delay_seconds} seconds")

        # Подключение к базе данных в новом потоке
        db_conn = connect_to_db()
        cursor = db_conn.cursor()

        # Проверка текущего статуса заказа перед обновлением
        query_check = "SELECT status_id FROM orders WHERE order_id = %s"
        cursor.execute(query_check, (order_id,))
        current_status = cursor.fetchone()
        cursor.close()

        if current_status and current_status[0] != 4:  # 4 - Cancelled
            cursor = db_conn.cursor()
            query = "UPDATE orders SET status_id = %s WHERE order_id = %s"
            cursor.execute(query, (new_status, order_id))
            db_conn.commit()
            cursor.close()
            print(f"Order {order_id} status updated to {new_status}")

            if new_status == 2:
                # После обновления статуса на "Out for Delivery", пытаемся назначить доставщика
                self.group_and_assign_orders()

                # Запускаем поток для обновления статуса "Delivered" после 5 секунд
                threading.Thread(target=self.update_order_status_after_delay, args=(order_id, 3, 5)).start()

    def cancel_order(self, order_id):
        cursor = self.db_connection.cursor()

        # Получаем время создания заказа и текущий статус
        query = "SELECT created_at, status_id FROM orders WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        cursor.close()

        if not result:
            print(f"Order {order_id} not found.")
            return False

        created_at, current_status = result
        elapsed_time = (datetime.now() - created_at).total_seconds()

        if elapsed_time > 5:
            print(f"Cannot cancel order {order_id}: время отмены истекло.")
            return False

        if current_status == 4:
            print(f"Order {order_id} уже отменен.")
            return False

        # Обновляем статус заказа на "Cancelled"
        cursor = self.db_connection.cursor()
        update_query = "UPDATE orders SET status_id = 4 WHERE order_id = %s"
        cursor.execute(update_query, (order_id,))
        self.db_connection.commit()
        cursor.close()
        print(f"Order {order_id} has been cancelled successfully.")
        return True

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

    def group_and_assign_orders(self):
        """
        Группирует заказы по почтовым индексам и назначает их доступным доставщикам.
        Максимум 3 пиццы в группе.
        """
        cursor = self.db_connection.cursor(dictionary=True)
        # Находим все заказы со статусом "Out for Delivery" (2) и без назначенного доставщика
        query = """
        SELECT o.order_id, o.customer_id, ca.postal_code_id
        FROM orders o
        JOIN customer_address ca ON o.customer_id = (SELECT customer_id FROM customer WHERE customer_id = o.customer_id)
        WHERE o.status_id = 2 AND o.delivery_person_id IS NULL
        ORDER BY o.created_at ASC
        """
        cursor.execute(query)
        pending_orders = cursor.fetchall()
        cursor.close()

        # Группируем заказы по postal_code_id
        from collections import defaultdict
        groups = defaultdict(list)
        for order in pending_orders:
            groups[order['postal_code_id']].append(order['order_id'])

        # Для каждой группы назначаем доставщика
        for postal_code_id, orders in groups.items():
            while len(orders) >= 1:
                # Формируем группу максимум из 3 пицц
                batch = orders[:3]
                orders = orders[3:]

                # Назначаем доступного доставщика для этого региона
                delivery_person = self.deliverymen_repo.find_available_delivery_person(postal_code_id)
                if delivery_person:
                    # Назначаем группу заказов этому доставщику
                    for order_id in batch:
                        self.assign_order_to_delivery_person(order_id, delivery_person['employee_id'])

                    # Обновляем статус доставщика на недоступный и запускаем таймер
                    self.deliverymen_repo.set_unavailable(delivery_person['employee_id'], delay_seconds=30)
                else:
                    print(f"No available delivery person for postal code {postal_code_id}")
                    break  # Нет доступных доставщиков для этого региона

    def assign_order_to_delivery_person(self, order_id, employee_id):
        cursor = self.db_connection.cursor()
        query = """
            UPDATE orders
            SET delivery_person_id = %s, estimated_delivery_time = NOW() + INTERVAL 30 MINUTE
            WHERE order_id = %s
        """
        cursor.execute(query, (employee_id, order_id))
        self.db_connection.commit()
        cursor.close()
        print(f'Order {order_id} assigned to delivery person {employee_id}.')