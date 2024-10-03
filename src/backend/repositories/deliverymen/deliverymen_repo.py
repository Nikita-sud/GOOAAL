# deliverymen_repo.py

from backend.repositories.deliverymen.deliverymen_intfc import DeliverymenInterface
import threading
import time

class DeliverymenRepo(DeliverymenInterface):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_delivery_person(self, employee_id, postal_code_id, availability=True, number_of_deliveries=0, last_delivery_time=None):
        cursor = self.db_connection.cursor()
        query = """
            INSERT INTO deliverymen (employee_id, postal_code_id, availability, number_of_deliverymen, last_delivery_time)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (employee_id, postal_code_id, availability, number_of_deliveries, last_delivery_time))
        self.db_connection.commit()
        cursor.close()
        print(f'Delivery person {employee_id} added successfully.')

    def remove_delivery_person(self, employee_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM deliverymen WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))
        self.db_connection.commit()
        cursor.close()
        print(f'Delivery person {employee_id} removed successfully.')

    def update_availability(self, employee_id, availability):
        cursor = self.db_connection.cursor()
        query = "UPDATE deliverymen SET availability = %s WHERE employee_id = %s"
        cursor.execute(query, (availability, employee_id))
        self.db_connection.commit()
        cursor.close()
        print(f'Availability for delivery person {employee_id} updated to {availability}.')

    def get_delivery_person_by_id(self, employee_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = "SELECT * FROM deliverymen WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))
        delivery_person = cursor.fetchone()
        cursor.close()
        return delivery_person

    def get_available_deliverymen_by_region(self, postal_code_id):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
            SELECT d.employee_id, d.postal_code_id, d.availability, d.number_of_deliverymen, d.last_delivery_time
            FROM deliverymen d
            WHERE d.postal_code_id = %s AND d.availability = 1
        """
        cursor.execute(query, (postal_code_id,))
        deliverymen = cursor.fetchall()
        cursor.close()
        return deliverymen

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

    def update_last_delivery_time(self, employee_id):
        cursor = self.db_connection.cursor()
        query = """
            UPDATE deliverymen
            SET last_delivery_time = NOW(), number_of_deliverymen = number_of_deliverymen + 1
            WHERE employee_id = %s
        """
        cursor.execute(query, (employee_id,))
        self.db_connection.commit()
        cursor.close()
        print(f'Last delivery time for delivery person {employee_id} updated.')

    def get_deliverymen_statistics(self):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
            SELECT d.employee_id, e.first_name, e.last_name, d.number_of_deliverymen, d.availability
            FROM deliverymen d
            JOIN employees e ON d.employee_id = e.employee_id
        """
        cursor.execute(query)
        stats = cursor.fetchall()
        cursor.close()
        return stats

    def find_available_delivery_person(self, postal_code_id):
        """
        Находит первого доступного доставщика для заданного почтового индекса.
        """
        available_deliverymen = self.get_available_deliverymen_by_region(postal_code_id)
        if available_deliverymen:
            return available_deliverymen[0]  # Возвращаем первого доступного
        return None

    def set_unavailable(self, employee_id, delay_seconds=30):
        self.update_availability(employee_id, False)
        print(f'Delivery person {employee_id} is now unavailable for {delay_seconds} seconds.')

        # Запускаем таймер, чтобы вернуть доступность после задержки
        threading.Thread(target=self.make_available_after_delay, args=(employee_id, delay_seconds)).start()

    def make_available_after_delay(self, employee_id, delay_seconds):
        time.sleep(delay_seconds)
        self.update_availability(employee_id, True)
        print(f'Delivery person {employee_id} is now available again.')