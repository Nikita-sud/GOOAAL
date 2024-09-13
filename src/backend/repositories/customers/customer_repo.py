
from datetime import datetime
from src.backend.repositories.customers.customer_intfc import CustomerInterface


class CustomerRepo(CustomerInterface):

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, name: str, last_name: str, gender: int, birthdate: str, phone:int, address:int):
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO customer (name, last_name, gender, birthdate, phone, address) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, last_name, gender, datetime.strptime(birthdate, '%d.%m.%Y').date(), phone, address))
        self.db_connection.commit()
        return

    def get_customer_by_id(self, id: int) ->(str):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM customer WHERE id = %s"
        cursor.execute(query, (id))
        return cursor.fetchone()
    
    def delete_customer(self, customer_id:int):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM customer WHERE id = %s"
        cursor.execute(query,(customer_id))
        self.db_connection.commit()
