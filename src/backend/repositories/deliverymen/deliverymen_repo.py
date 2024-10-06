# deliverymen_repo.py

from backend.repositories.deliverymen.deliverymen_intfc import DeliverymenInterface
import threading
import time
from backend.database import connect_to_db

# Defining the DeliverymenRepo class that implements the DeliverymenInterface
class DeliverymenRepo(DeliverymenInterface):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Method to add a new delivery person to the database
    def add_delivery_person(self, employee_id, restaurant_id, availability=True, number_of_deliveries=0, last_delivery_time=None):
        cursor = self.db_connection.cursor()
        query = """
            INSERT INTO deliverymen (employee_id, restaurant_id, availability, number_of_deliveries, last_delivery_time)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (employee_id, restaurant_id, availability, number_of_deliveries, last_delivery_time))
        self.db_connection.commit()
        cursor.close()
        print(f'Delivery person {employee_id} added successfully.')

    # Method to remove a delivery person from the database by employee ID
    def remove_delivery_person(self, employee_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM deliverymen WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
        print(f'Delivery person {employee_id} removed successfully.')

    # Method to update the availability status of a delivery person
    def update_availability(self, employee_id, availability, db_conn=None):
        """
        Updates the availability status of a delivery person.
        
        Args:
            employee_id: The ID of the delivery person.
            availability: The availability status (True or False).
            db_conn: Database connection to use.
        """
        if db_conn is None:
            db_conn = self.db_connection

        cursor = db_conn.cursor()
        query = "UPDATE deliverymen SET availability = %s WHERE employee_id = %s"
        cursor.execute(query, (availability, employee_id))
        db_conn.commit()  # Commit the changes to the database
        cursor.close()
        print(f'Availability for delivery person {employee_id} updated to {availability}.')


    # Method to get details of a delivery person by employee ID
    def get_delivery_person_by_id(self, employee_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = "SELECT * FROM deliverymen WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))  # Execute query with the given employee ID
        delivery_person = cursor.fetchone()  # Fetch one result from the executed query
        cursor.close()  # Close the cursor
        return delivery_person  # Return delivery person details as a dictionary

    # Method to get available delivery persons by region (postal code ID)
    def get_available_deliverymen_by_restaurant(self, restaurant_id, db_conn):
        """
        Retrieves available delivery personnel for a specific restaurant.
        
        Args:
            restaurant_id: The ID of the restaurant.
            db_conn: Database connection to use.
        
        Returns:
            list: A list of available delivery personnel.
        """
        cursor = db_conn.cursor(dictionary=True)
        query = """
            SELECT d.employee_id, d.restaurant_id, d.availability, d.number_of_deliveries, d.last_delivery_time
            FROM deliverymen d
            WHERE d.restaurant_id = %s AND d.availability = 1
        """
        cursor.execute(query, (restaurant_id,))
        deliverymen = cursor.fetchall()
        cursor.close()
        return deliverymen

    # Method to assign an order to a delivery person
    def assign_order_to_delivery_person(self, order_id, employee_id):
        cursor = self.db_connection.cursor()
        query = """
            UPDATE orders
            SET delivery_person_id = %s, estimated_delivery_time = NOW() + INTERVAL 30 MINUTE
            WHERE order_id = %s
        """
        cursor.execute(query, (employee_id, order_id))  # Assign order to the delivery person and set estimated delivery time
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
        print(f'Order {order_id} assigned to delivery person {employee_id}.')

    # Method to update the last delivery time for a delivery person
    def update_last_delivery_time(self, employee_id):
        cursor = self.db_connection.cursor()
        query = """
            UPDATE deliverymen
            SET last_delivery_time = NOW(), number_of_deliveries = number_of_deliveries + 1
            WHERE employee_id = %s
        """
        cursor.execute(query, (employee_id,))
        self.db_connection.commit()
        cursor.close()
        print(f'Last delivery time for delivery person {employee_id} updated.')

    # Method to get delivery statistics of all deliverymen
    def get_deliverymen_statistics(self):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
            SELECT d.employee_id, e.first_name, e.last_name, d.number_of_deliveries, d.availability
            FROM deliverymen d
            JOIN employees e ON d.employee_id = e.employee_id
        """
        cursor.execute(query)
        stats = cursor.fetchall()
        cursor.close()
        return stats

    # Method to find the first available delivery person for a given postal code
    def find_available_delivery_person(self, restaurant_id, db_conn):
        """
        Finds an available delivery person for a given restaurant.

        Args:
            restaurant_id: The ID of the restaurant.
            db_conn: Database connection to use.

        Returns:
            dict or None: The delivery person's details or None if not found.
        """
        available_deliverymen = self.get_available_deliverymen_by_restaurant(restaurant_id, db_conn)
        if available_deliverymen:
            return available_deliverymen[0]
        return None

    # Method to set a delivery person as unavailable for a specified delay
    def set_unavailable(self, employee_id, db_conn=None):
        """
        Sets a delivery person as unavailable.
        
        Args:
            employee_id: The ID of the delivery person.
            db_conn: Database connection to use.
        """
        if db_conn is None:
            db_conn = self.db_connection

        self.update_availability(employee_id, False, db_conn=db_conn)
        print(f'Delivery person {employee_id} is now unavailable.')

    def set_available_after_delay(self, employee_id, delay_seconds=30):
        """
        Schedules the delivery person to become available after a specified delay.
        
        Args:
            employee_id: The ID of the delivery person.
            delay_seconds: The delay in seconds before making them available again.
        """
        threading.Thread(target=self.make_available_after_delay, args=(employee_id, delay_seconds)).start()

    def make_available_after_delay(self, employee_id, delay_seconds):
        """
        Makes a delivery person available again after a specified delay.
        
        Args:
            employee_id: The ID of the delivery person.
            delay_seconds: The delay in seconds.
        """
        time.sleep(delay_seconds)  # Wait for the specified delay
        db_conn = connect_to_db()
        try:
            self.update_availability(employee_id, True, db_conn=db_conn)  # Set availability to True
            print(f'Delivery person {employee_id} is now available again.')
        finally:
            db_conn.close()  # Close the database connection