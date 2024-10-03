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
    
    def set_discount_for_next(self, customer_id, discount):
        cursor = self.db_connection.cursor()
        query = "UPDATE customer SET discount_for_next = %s WHERE customer_id = %s"
        cursor.execute(query, (discount,customer_id,))
        print(f'Discount was added {discount}')
        cursor.close()
        self.db_connection.commit()  

    def get_discount_for_next(self, customer_id):
        cursor = self.db_connection.cursor()
        query = "SELECT discount_for_next FROM customer WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        print(f'Discount: {result[0]}')
        cursor.close()
        return float(result[0])
    
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
        INSERT INTO customer_address (house_number, apartment_number, postal_code_id)
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

    def get_customer_by_id(self, id: int) -> dict:
        cursor = self.db_connection.cursor()
        query = """
            SELECT c.name, c.last_name, ca.house_number, ca.apartment_number, pc.street, pc.postal_code
            FROM customer c
            JOIN customer_address ca ON c.address = ca.customer_address_id
            JOIN postal_codes pc ON ca.postal_code_id = pc.ID
            WHERE c.customer_id = %s
        """
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return {
                'name': result[0],
                'last_name': result[1],
                'address': f"{result[4]} {result[2]}, {result[3]} - {result[5]}"
            }
        return None
    
    def update_customer_num_of_orders(self, id: int):
        cursor = self.db_connection.cursor()
        query = "UPDATE customer SET number_orders = number_orders+1 WHERE customer_id = %s"
        cursor.execute(query, (id,))
        self.db_connection.commit()        
        return 
    
    def create_hashed_password_salt(self,password):
        salt = os.urandom(4)

        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return [hashed_password.hex(), salt.hex()]
 
    
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

    def get_customer_by_id(self, id: int) -> dict:
        cursor = self.db_connection.cursor()
        query = """
            SELECT c.name, c.last_name, ca.house_number, ca.apartment_number, pc.postal_code
            FROM customer c
            JOIN customer_address ca ON c.address = ca.customer_address_id
            JOIN postal_codes pc ON ca.postal_code_id = pc.ID
            WHERE c.customer_id = %s
        """
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return {
                'name': result[0],
                'last_name': result[1],
                'address': f"{result[2]}, {result[3]} - {result[4]}"
            }
        return None