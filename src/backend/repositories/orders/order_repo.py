# order_repo.py

from backend.database import connect_to_db
from backend.repositories.orders.order_intfc import OrderInterface
from backend.models import Order
import threading
import time
from datetime import datetime
from collections import defaultdict


# Defining the OrderRepo class that implements the OrderInterface
class OrderRepo(OrderInterface):
    """
    Repository class for managing orders. Implements the OrderInterface.
    Handles operations such as saving orders, updating order statuses,
    cancelling orders, and assigning delivery personnel.
    """

    def __init__(self, db_connection, deliverymen_repo):
        """
        Initializes the OrderRepo with a database connection and a deliverymen repository.
        
        Args:
            db_connection: Database connection object.
            deliverymen_repo: Repository for managing delivery personnel.
        """
        self.db_connection = db_connection
        self.deliverymen_repo = deliverymen_repo  # Repository for managing deliverymen

    def save_order(self, order: Order):
        """
        Saves an order and its items to the database. Sets default status and creation date
        if not provided. After saving, initiates a thread to update the order status after a delay.
        
        Args:
            order (Order): The order object to be saved.
        """
        cursor = self.db_connection.cursor()

        # Set default status if not specified
        if not hasattr(order, 'status_id'):
            order.status_id = 1  # Example: 1 represents "Being Prepared"

        # Set creation date if not specified
        if not hasattr(order, 'created_at'):
            order.created_at = datetime.now()

        # Insert the order into the orders table
        query = """
        INSERT INTO orders (customer_id, total_price, status_id, created_at, discount_applied)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (order.customer_id, order.total_price, order.status_id, order.created_at, order.discount_applied))
        self.db_connection.commit()  # Commit the changes to the database
        order.order_id = cursor.lastrowid  # Get the ID of the created order

        # Save order items
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
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor

        # Start a thread to update the order status after a delay
        threading.Thread(target=self.update_order_status_after_delay, args=(order.order_id, 2, 5)).start()

    def update_order_status_after_delay(self, order_id, new_status, delay_seconds):
        time.sleep(delay_seconds)
        print(f"Updating order {order_id} to status {new_status} after {delay_seconds} seconds")

        db_conn = connect_to_db()

        try:
            cursor = db_conn.cursor()

            # Fetch current status and delivery person assignment
            query_check = "SELECT status_id, delivery_person_id FROM orders WHERE order_id = %s"
            cursor.execute(query_check, (order_id,))
            result = cursor.fetchone()
            cursor.close()

            if result and result[0] != 4:  # Check if not cancelled
                current_status_id, delivery_person_id = result

                if new_status == 3:
                    if not delivery_person_id:
                        # Cannot update to Delivered without a delivery person
                        print(f"Order {order_id} cannot be updated to Delivered as no delivery person is assigned.")
                        return

                    # Update order status to Delivered
                    cursor = db_conn.cursor()
                    query = "UPDATE orders SET status_id = %s WHERE order_id = %s"
                    cursor.execute(query, (new_status, order_id))
                    db_conn.commit()
                    cursor.close()
                    print(f"Order {order_id} status updated to {new_status}")

                    # Schedule the delivery person's availability to reset after 30 seconds
                    self.deliverymen_repo.set_available_after_delay(delivery_person_id, 30)
                elif new_status == 2:
                    # Update order status to Out for Delivery
                    cursor = db_conn.cursor()
                    query = "UPDATE orders SET status_id = %s WHERE order_id = %s"
                    cursor.execute(query, (new_status, order_id))
                    db_conn.commit()
                    cursor.close()
                    print(f"Order {order_id} status updated to {new_status}")

                    # Attempt to assign a delivery person
                    self.group_and_assign_orders(db_conn)

                    # Check if a delivery person was assigned
                    cursor = db_conn.cursor()
                    query_check_delivery = "SELECT delivery_person_id FROM orders WHERE order_id = %s"
                    cursor.execute(query_check_delivery, (order_id,))
                    delivery_result = cursor.fetchone()
                    cursor.close()

                    if delivery_result and delivery_result[0]:
                        # Schedule to update status to Delivered after delivery time
                        threading.Thread(target=self.update_order_status_after_delay, args=(order_id, 3, 5)).start()
                    else:
                        print(f"No delivery person assigned to order {order_id}; cannot proceed to Delivered status.")
                else:
                    # For other statuses, simply update
                    cursor = db_conn.cursor()
                    query = "UPDATE orders SET status_id = %s WHERE order_id = %s"
                    cursor.execute(query, (new_status, order_id))
                    db_conn.commit()
                    cursor.close()
                    print(f"Order {order_id} status updated to {new_status}")
        finally:
            db_conn.close()

    def cancel_order(self, order_id):
        """
        Cancels an order if it is within the allowable cancellation time and not already cancelled.
        
        Args:
            order_id (int): The ID of the order to cancel.
        
        Returns:
            bool: True if the order was successfully cancelled, False otherwise.
        """
        cursor = self.db_connection.cursor()

        # Get the creation time and current status of the order
        query = "SELECT created_at, status_id FROM orders WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        cursor.close()  # Close the cursor

        if not result:
            print(f"Order {order_id} not found.")
            return False

        created_at, current_status = result
        elapsed_time = (datetime.now() - created_at).total_seconds()

        # Check if the cancellation is within the allowed time frame (e.g., 5 seconds)
        if elapsed_time > 5:
            print(f"Cannot cancel order {order_id}: cancellation time has expired.")
            return False

        # Check if the order is already cancelled
        if current_status == 4:
            print(f"Order {order_id} is already cancelled.")
            return False

        # Update the order status to "Cancelled"
        cursor = self.db_connection.cursor()
        update_query = "UPDATE orders SET status_id = 4 WHERE order_id = %s"
        cursor.execute(update_query, (order_id,))
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
        print(f"Order {order_id} has been cancelled successfully.")
        return True

    def get_order_by_id(self, order_id):
        """
        Retrieves an order by its ID.
        
        Args:
            order_id (int): The ID of the order to retrieve.
        
        Returns:
            dict or None: The order details as a dictionary if found, else None.
        """
        cursor = self.db_connection.cursor(dictionary=True)
        query = "SELECT * FROM orders WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        order = cursor.fetchone()  # Fetch one result from the executed query
        cursor.close()  # Close the cursor
        return order  # Return the order details as a dictionary

    def get_orders_by_customer_id(self, customer_id):
        """
        Retrieves all orders for a given customer, ordered by creation date descending.
        
        Args:
            customer_id (int): The ID of the customer whose orders are to be retrieved.
        
        Returns:
            list: A list of orders as dictionaries.
        """
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT o.order_id, o.total_price, o.created_at, os.status_name
        FROM orders o
        JOIN order_status os ON o.status_id = os.status_id
        WHERE o.customer_id = %s
        ORDER BY o.created_at DESC
        """
        cursor.execute(query, (customer_id,))
        orders = cursor.fetchall()  # Fetch all orders for the customer
        cursor.close()  # Close the cursor
        return orders  # Return the list of orders

    def get_order_details(self, order_id):
        """
        Retrieves detailed information about an order, including its items.
        
        Args:
            order_id (int): The ID of the order to retrieve details for.
        
        Returns:
            dict: A dictionary containing order information and its items.
        """
        cursor = self.db_connection.cursor(dictionary=True)

        # Retrieve order information, including status_id
        order_query = """
        SELECT o.order_id, o.customer_id, o.total_price, o.created_at, o.status_id, os.status_name
        FROM orders o
        JOIN order_status os ON o.status_id = os.status_id
        WHERE o.order_id = %s
        """
        cursor.execute(order_query, (order_id,))
        order = cursor.fetchone()

        if order:
            print(f"Fetched order: status_id={order['status_id']}, status_name={order['status_name']}")
        else:
            print(f"Order {order_id} not found.")

        # Retrieve order items
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

        # Convert data types for items
        for item in items:
            item['price'] = float(item['price'])
            item['quantity'] = int(item['quantity'])

        # Convert total_price to float
        if order:
            order['total_price'] = float(order['total_price'])

        cursor.close()
        return {'order': order, 'items': items}

    def get_all_orders(self):
        """
        Retrieves all orders in the system, ordered by creation date descending.
        
        Returns:
            list: A list of all orders as dictionaries.
        """
        cursor = self.db_connection.cursor(dictionary=True)
        query = """SELECT o.order_id, o.total_price, o.created_at, os.status_name
        FROM orders o 
        JOIN order_status os ON o.status_id = os.status_id
        ORDER BY o.created_at DESC"""
        cursor.execute(query)
        orders = cursor.fetchall()  # Fetch all orders in the system
        cursor.close()  # Close the cursor
        return orders  # Return the list of all orders

    def group_and_assign_orders(self, db_conn):
        """
        Groups pending orders and assigns them to available delivery personnel.

        Args:
            db_conn: Database connection to use within the thread.
        """
        cursor = db_conn.cursor(dictionary=True)
        # Find all orders with status "Out for Delivery" (2) and without an assigned delivery person
        query = """
        SELECT o.order_id, o.customer_id, ca.postal_code_id, r.restaurant_id
        FROM orders o
        JOIN customer c ON o.customer_id = c.customer_id
        JOIN customer_address ca ON c.address = ca.customer_address_id
        JOIN restaurants r ON ca.postal_code_id BETWEEN r.postal_code_cover_from AND r.postal_code_cover_till
        WHERE o.status_id = 2 AND o.delivery_person_id IS NULL
        ORDER BY o.created_at ASC
        """
        cursor.execute(query)
        pending_orders = cursor.fetchall()
        cursor.close()

        # Group orders by restaurant_id
        groups = defaultdict(list)
        for order in pending_orders:
            groups[order['restaurant_id']].append(order['order_id'])

        # Assign delivery persons to each group
        for restaurant_id, orders in groups.items():
            while len(orders) >= 1:
                batch = orders[:3]
                orders = orders[3:]

                delivery_person = self.deliverymen_repo.find_available_delivery_person(restaurant_id, db_conn)
                if delivery_person:
                    for order_id in batch:
                        self.assign_order_to_delivery_person(order_id, delivery_person['employee_id'], db_conn)

                    # Set the delivery person as unavailable
                    self.deliverymen_repo.set_unavailable(delivery_person['employee_id'], db_conn=db_conn)
                else:
                    print(f"No available delivery person for restaurant {restaurant_id}")
                    break

    def assign_order_to_delivery_person(self, order_id, employee_id, db_conn):
        """
        Assigns an order to a delivery person and sets the estimated delivery time.
        
        Args:
            order_id (int): The ID of the order to assign.
            employee_id (int): The ID of the delivery person.
            db_conn: Database connection to use within the thread.
        """
        cursor = db_conn.cursor()
        query = """
            UPDATE orders
            SET delivery_person_id = %s, estimated_delivery_time = NOW() + INTERVAL 30 MINUTE
            WHERE order_id = %s
        """
        cursor.execute(query, (employee_id, order_id))  # Assign the delivery person and set estimated delivery time
        db_conn.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
        print(f'Order {order_id} assigned to delivery person {employee_id}.')