
from datetime import datetime
from backend.repositories.customers.customer_intfc import CustomerInterface
import os
import hashlib


class CustomerRepo(CustomerInterface):

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, name: str, last_name: str, gender: int, birthdate: str, phone:str, address:int):
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
        cursor.execute(query, (id,))
        return cursor.fetchone()
    
    def create_credentials(self, username:str, password:str):
        cursor = self.db_connection.cursor()

        get_last_pk = "SELECT LAST_INSERT_ID()"
        cursor.execute(get_last_pk)
        customer_id = cursor.fetchone()[0]
        print(customer_id)

        query = """
            INSERT INTO credentials (customer_id, username, password, salt) VALUES(%s, %s, %s, %s)
            """
        salt = os.urandom(4)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        cursor.execute(query, (customer_id, username, hashed_password, salt,))
        self.db_connection.commit()
        cursor.close()
        return
    
    def check_user(self, username:str, password:str) -> (bool):
        cursor = self.db_connection.cursor()
        query = """
        SELECT password, salt
        FROM credentials
        WHERE username = %s
        """
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()

        if(result == None):
            return False
        stored_password, stored_salt = result
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)
        if hashed_password == stored_password:
            return True
        else:
            return False
        return
    
    def delete_customer(self, customer_id:int):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM customer WHERE customer_id = %s"
        cursor.execute(query,(customer_id,))
        self.db_connection.commit()
