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
        """
        Updates the status of an order after a specified delay. If the new status is 'Out for Delivery',
        it also attempts to assign a delivery person and schedules another status update to 'Delivered'.
        
        Args:
            order_id (int): The ID of the order to update.
            new_status (int): The new status ID to set.
            delay_seconds (int): The delay in seconds before updating the status.
        """
        time.sleep(delay_seconds)  # Wait for the specified delay
        print(f"Updating order {order_id} to status {new_status} after {delay_seconds} seconds")

        # Connect to the database in the new thread
        db_conn = connect_to_db()
        cursor = db_conn.cursor()

        # Check the current status of the order before updating
        query_check = "SELECT status_id FROM orders WHERE order_id = %s"
        cursor.execute(query_check, (order_id,))
        current_status = cursor.fetchone()
        cursor.close()  # Close the cursor

        if current_status and current_status[0] != 4:  # 4 represents "Cancelled"
            cursor = db_conn.cursor()
            query = "UPDATE orders SET status_id = %s WHERE order_id = %s"
            cursor.execute(query, (new_status, order_id))
            db_conn.commit()  # Commit the changes to the database
            cursor.close()  # Close the cursor
            print(f"Order {order_id} status updated to {new_status}")

            if new_status == 2:
                # After updating the status to "Out for Delivery", attempt to assign a delivery person
                self.group_and_assign_orders()

                # Start a thread to update the status to "Delivered" after 5 seconds
                threading.Thread(target=self.update_order_status_after_delay, args=(order_id, 3, 5)).start()

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

    def group_and_assign_orders(self):
        """
        Groups orders by postal codes and assigns them to available delivery personnel.
        Each delivery person can handle up to 3 orders at a time. After assignment, the delivery
        person is marked as unavailable for a specified duration.
        """
        cursor = self.db_connection.cursor(dictionary=True)
        # Find all orders with status "Out for Delivery" (2) and without an assigned delivery person
        query = """
        SELECT o.order_id, o.customer_id, ca.postal_code_id
        FROM orders o
        JOIN customer_address ca ON o.customer_id = (SELECT customer_id FROM customer WHERE customer_id = o.customer_id)
        WHERE o.status_id = 2 AND o.delivery_person_id IS NULL
        ORDER BY o.created_at ASC
        """
        cursor.execute(query)
        pending_orders = cursor.fetchall()  # Fetch all pending orders
        cursor.close()  # Close the cursor

        # Group orders by postal_code_id
        groups = defaultdict(list)
        for order in pending_orders:
            groups[order['postal_code_id']].append(order['order_id'])

        # Assign delivery persons to each group
        for postal_code_id, orders in groups.items():
            while len(orders) >= 1:
                # Form a batch of up to 3 orders
                batch = orders[:3]
                orders = orders[3:]

                # Find an available delivery person for this region
                delivery_person = self.deliverymen_repo.find_available_delivery_person(postal_code_id)
                if delivery_person:
                    # Assign the batch of orders to this delivery person
                    for order_id in batch:
                        self.assign_order_to_delivery_person(order_id, delivery_person['employee_id'])

                    # Set the delivery person as unavailable and start a timer
                    self.deliverymen_repo.set_unavailable(delivery_person['employee_id'], delay_seconds=30)
                else:
                    print(f"No available delivery person for postal code {postal_code_id}")
                    break  # No available delivery persons for this region

    def assign_order_to_delivery_person(self, order_id, employee_id):
        """
        Assigns an order to a delivery person and sets the estimated delivery time.
        
        Args:
            order_id (int): The ID of the order to assign.
            employee_id (int): The ID of the delivery person.
        """
        cursor = self.db_connection.cursor()
        query = """
            UPDATE orders
            SET delivery_person_id = %s, estimated_delivery_time = NOW() + INTERVAL 30 MINUTE
            WHERE order_id = %s
        """
        cursor.execute(query, (employee_id, order_id))  # Assign the delivery person and set estimated delivery time
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
        print(f'Order {order_id} assigned to delivery person {employee_id}.')