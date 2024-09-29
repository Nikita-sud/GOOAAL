# customer_repo.py
from datetime import datetime
from backend.repositories.customers.customer_intfc import CustomerInterface
import os
import hashlib


class CustomerRepo(CustomerInterface):

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_customer_id(self, username):
        cursor = self.db_connection.cursor()
        query = "SELECT customer_id FROM credentials WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None
    
    def get_postal_code_id(self, postal_code):
        cursor = self.db_connection.cursor()

        query = """SELECT ID FROM postal_codes
        WHERE postal_code = %s"""
        cursor.execute(query, (postal_code,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]



    def create_user(self, name: str, last_name: str, gender: int, birthdate: str, phone:str,street_number, apartment_number, postal_code, new_username, new_password):
        postal_code_id = self.get_postal_code_id(postal_code)

        # query = """
        #     START TRANSACTION;
            
        #     INSERT INTO customer_address(street_number, apartment_number, postal_code_id)
        #     VALUES (%s, %s, %s);

        #     SET @address_id = LAST_INSERT_ID();

        #     INSERT INTO customer (name, last_name, gender_id, birthdate, phone, address)
        #     VALUES (%s, %s, %s, %s, %s, @address_id);

        #     SET @customer_id = LAST_INSERT_ID();

        #     INSERT INTO credentials (customer_id, username, password, salt)
        #     VALUES(@customer_id, %s, %s, %s);
            
        #     COMMIT;
        # """
        cursor = self.db_connection.cursor()

        cursor.execute("START TRANSACTION;")
        cursor.execute("""
        INSERT INTO customer_address (street_number, apartment_number, postal_code_id)
        VALUES (%s, %s, %s);
    """, (street_number, apartment_number, postal_code_id))
        cursor.execute("SET @address_id = LAST_INSERT_ID();")
        cursor.execute("""
                INSERT INTO customer (name, last_name, gender_id, birthdate, phone, address)
                VALUES (%s, %s, %s, %s, %s, @address_id);
            """, (name, last_name, gender, datetime.strptime(birthdate, '%d.%m.%Y').date(), phone))
        cursor.execute("SET @customer_id = LAST_INSERT_ID();")


        hashed_password_and_salt= self.create_hashed_password_salt(new_password)
        cursor.execute("""
        INSERT INTO credentials (customer_id, username, password, salt)
        VALUES (@customer_id, %s, %s, %s);
        """, (new_username, hashed_password_and_salt[0], hashed_password_and_salt[1]))

        # cursor.execute(query, (street_number,apartment_number, postal_code_id,name, last_name, gender, datetime.strptime(birthdate, '%d.%m.%Y').date(), phone, new_username, hashed_password_and_salt[0], hashed_password_and_salt[1]), multi=True)
        cursor.execute("COMMIT;")
        
        self.db_connection.commit()        
        return

    def get_customer_by_id(self, id: int) ->(str):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM customer WHERE id = %s"
        cursor.execute(query, (id,))
        return cursor.fetchone()
    
    def create_hashed_password_salt(self,password):
        salt = os.urandom(4)

        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return [hashed_password.hex(), salt.hex()]
    
    # def create_credentials(self, username:str, password:str):
    #     cursor = self.db_connection.cursor()

    #     get_last_pk = "SELECT LAST_INSERT_ID()"
    #     cursor.execute(get_last_pk)
    #     customer_id = cursor.fetchone()[0]
    #     print(customer_id)

    #     query = """
    #         INSERT INTO credentials (customer_id, username, password, salt) VALUES(%s, %s, %s, %s)
    #         """
    #     salt = os.urandom(4)
    #     hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    #     cursor.execute(query, (customer_id, username, hashed_password.hex(), salt.hex(),))
    #     self.db_connection.commit()
    #     cursor.close()
    #     return
    
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
        stored_password_hex, stored_salt_hex = result
        stored_password = bytes.fromhex(stored_password_hex)
        stored_salt = bytes.fromhex(stored_salt_hex)
        
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

    def update_number_orders(self, customer_id: int, number_orders: int):
        cursor = self.db_connection.cursor()
        query = "UPDATE customer SET number_orders = %s WHERE customer_id = %s"
        cursor.execute(query, (number_orders, customer_id))
        self.db_connection.commit()
        cursor.close()