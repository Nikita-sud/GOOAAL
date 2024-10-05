# deliverymen_repo.py

from backend.repositories.deliverymen.deliverymen_intfc import DeliverymenInterface
import threading
import time

# Defining the DeliverymenRepo class that implements the DeliverymenInterface
class DeliverymenRepo(DeliverymenInterface):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Method to add a new delivery person to the database
    def add_delivery_person(self, employee_id, postal_code_id, availability=True, number_of_deliveries=0, last_delivery_time=None):
        cursor = self.db_connection.cursor()
        query = """
            INSERT INTO deliverymen (employee_id, postal_code_id, availability, number_of_deliverymen, last_delivery_time)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (employee_id, postal_code_id, availability, number_of_deliveries, last_delivery_time))
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
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
    def update_availability(self, employee_id, availability):
        cursor = self.db_connection.cursor()
        query = "UPDATE deliverymen SET availability = %s WHERE employee_id = %s"
        cursor.execute(query, (availability, employee_id))
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
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
    def get_available_deliverymen_by_region(self, postal_code_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
            SELECT d.employee_id, d.postal_code_id, d.availability, d.number_of_deliverymen, d.last_delivery_time
            FROM deliverymen d
            WHERE d.postal_code_id = %s AND d.availability = 1
        """
        cursor.execute(query, (postal_code_id,))  # Execute query with the given postal code ID
        deliverymen = cursor.fetchall()  # Fetch all available deliverymen
        cursor.close()  # Close the cursor
        return deliverymen  # Return list of available deliverymen

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
            SET last_delivery_time = NOW(), number_of_deliverymen = number_of_deliverymen + 1
            WHERE employee_id = %s
        """
        cursor.execute(query, (employee_id,))  # Update last delivery time and increment number of deliveries
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
        print(f'Last delivery time for delivery person {employee_id} updated.')

    # Method to get delivery statistics of all deliverymen
    def get_deliverymen_statistics(self):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
            SELECT d.employee_id, e.first_name, e.last_name, d.number_of_deliverymen, d.availability
            FROM deliverymen d
            JOIN employees e ON d.employee_id = e.employee_id
        """
        cursor.execute(query)  # Execute the query to get statistics
        stats = cursor.fetchall()  # Fetch all deliverymen statistics
        cursor.close()  # Close the cursor
        return stats  # Return statistics as a list of dictionaries

    # Method to find the first available delivery person for a given postal code
    def find_available_delivery_person(self, postal_code_id):
        available_deliverymen = self.get_available_deliverymen_by_region(postal_code_id)  # Get available deliverymen by region
        if available_deliverymen:
            return available_deliverymen[0]  # Return the first available delivery person
        return None  # Return None if no delivery person is available

    # Method to set a delivery person as unavailable for a specified delay
    def set_unavailable(self, employee_id, delay_seconds=30):
        self.update_availability(employee_id, False)  # Set availability to False
        print(f'Delivery person {employee_id} is now unavailable for {delay_seconds} seconds.')

        # Start a timer to make the delivery person available again after the delay
        threading.Thread(target=self.make_available_after_delay, args=(employee_id, delay_seconds)).start()

    # Method to make a delivery person available again after a delay
    def make_available_after_delay(self, employee_id, delay_seconds):
        time.sleep(delay_seconds)  # Wait for the specified delay
        self.update_availability(employee_id, True)  # Set availability to True
        print(f'Delivery person {employee_id} is now available again.')