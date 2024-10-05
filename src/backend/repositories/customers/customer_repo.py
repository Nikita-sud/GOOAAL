# customer_repo.py
# Importing necessary libraries
from datetime import datetime
from backend.repositories.customers.customer_intfc import CustomerInterface
import os
import hashlib

# Defining the CustomerRepo class that inherits from CustomerInterface
class CustomerRepo(CustomerInterface):

    # Initializing the repository with a database connection
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Method to get customer ID by username
    def get_customer_id(self, username):
        cursor = self.db_connection.cursor()
        query = "SELECT customer_id FROM credentials WHERE username = %s"
        cursor.execute(query, (username,))  # Execute query with the given username
        result = cursor.fetchone()  # Fetch one result from the executed query
        cursor.close()  # Close the cursor
        return result[0] if result else None  # Return customer ID if found, else None
    
    # Method to set a discount for the next purchase for a customer
    def set_discount_for_next(self, customer_id, discount):
        cursor = self.db_connection.cursor()
        query = "UPDATE customer SET discount_for_next = %s WHERE customer_id = %s"
        cursor.execute(query, (discount, customer_id,))  # Execute update query with discount and customer ID
        print(f'Discount was added {discount}')  # Print confirmation message
        cursor.close()  # Close the cursor
        self.db_connection.commit()  # Commit the changes to the database

    # Method to get discount for the next purchase for a customer
    def get_discount_for_next(self, customer_id):
        cursor = self.db_connection.cursor()
        query = "SELECT discount_for_next FROM customer WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))  # Execute query with the given customer ID
        result = cursor.fetchone()  # Fetch one result from the executed query
        print(f'Discount: {result[0]}')  # Print the discount value
        cursor.close()  # Close the cursor
        return float(result[0])  # Return discount as a float value
    
    # Method to get postal code ID by postal code
    def get_postal_code_id(self, postal_code):
        cursor = self.db_connection.cursor()
        query = """SELECT ID FROM postal_codes
        WHERE postal_code = %s"""
        cursor.execute(query, (postal_code,))  # Execute query with the given postal code
        result = cursor.fetchone()  # Fetch one result from the executed query
        cursor.close()  # Close the cursor
        return result[0]  # Return postal code ID

    # Method to create a new user with all required details
    def create_user(self, name: str, last_name: str, gender: int, birthdate: str, phone: str, street_number, apartment_number, postal_code, new_username, new_password):
        # Get postal code ID for the given postal code
        postal_code_id = self.get_postal_code_id(postal_code)
        cursor = self.db_connection.cursor()

        # Start a transaction to ensure data consistency
        cursor.execute("START TRANSACTION;")
        cursor.execute("""
        INSERT INTO customer_address (house_number, apartment_number, postal_code_id)
        VALUES (%s, %s, %s);
        """, (street_number, apartment_number, postal_code_id))  # Insert customer address details
        cursor.execute("SET @address_id = LAST_INSERT_ID();")  # Get the last inserted address ID
        cursor.execute("""
                INSERT INTO customer (name, last_name, gender_id, birthdate, phone, address)
                VALUES (%s, %s, %s, %s, %s, @address_id);
            """, (name, last_name, gender, datetime.strptime(birthdate, '%d.%m.%Y').date(), phone))  # Insert customer details
        cursor.execute("SET @customer_id = LAST_INSERT_ID();")  # Get the last inserted customer ID

        # Create hashed password with salt
        hashed_password_and_salt = self.create_hashed_password_salt(new_password)
        cursor.execute("""
        INSERT INTO credentials (customer_id, username, password, salt)
        VALUES (@customer_id, %s, %s, %s);
        """, (new_username, hashed_password_and_salt[0], hashed_password_and_salt[1]))  # Insert credentials

        # Commit the transaction
        cursor.execute("COMMIT;")
        
        self.db_connection.commit()  # Commit the transaction to the database       
        return

    # Method to get customer details by customer ID
    def get_customer_by_id(self, id: int) -> dict:
        cursor = self.db_connection.cursor()
        query = """
            SELECT c.name, c.last_name, ca.house_number, ca.apartment_number, pc.street, pc.postal_code
            FROM customer c
            JOIN customer_address ca ON c.address = ca.customer_address_id
            JOIN postal_codes pc ON ca.postal_code_id = pc.ID
            WHERE c.customer_id = %s
        """
        cursor.execute(query, (id,))  # Execute query with the given customer ID
        result = cursor.fetchone()  # Fetch one result from the executed query
        cursor.close()  # Close the cursor

        # Return customer details in dictionary format if found
        if result:
            return {
                'name': result[0],
                'last_name': result[1],
                'address': f"{result[4]} {result[2]}, {result[3]} - {result[5]}"
            }
        return None  # Return None if customer not found
    
    # Method to update the number of orders for a customer
    def update_customer_num_of_orders(self, id: int):
        cursor = self.db_connection.cursor()
        query = "UPDATE customer SET number_orders = number_orders+1 WHERE customer_id = %s"
        cursor.execute(query, (id,))  # Increment the number of orders by 1 for the given customer ID
        self.db_connection.commit()  # Commit the changes to the database       
        return
    
    # Method to create a hashed password along with a salt
    def create_hashed_password_salt(self, password):
        salt = os.urandom(4)  # Generate a random salt (4 bytes)

        # Hash the password using PBKDF2-HMAC with SHA-256, salt, and 100,000 iterations
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return [hashed_password.hex(), salt.hex()]  # Return hashed password and salt as hex strings

    # Method to check if a user exists and validate the password
    def check_user(self, username: str, password: str) -> (bool):
        cursor = self.db_connection.cursor()
        query = """
        SELECT password, salt
        FROM credentials
        WHERE username = %s
        """
        cursor.execute(query, (username,))  # Execute query with the given username
        result = cursor.fetchone()  # Fetch one result from the executed query
        cursor.close()  # Close the cursor

        if result == None:
            return False  # Return False if user not found
        
        stored_password_hex, stored_salt_hex = result
        stored_password = bytes.fromhex(stored_password_hex)  # Convert stored password from hex to bytes
        stored_salt = bytes.fromhex(stored_salt_hex)  # Convert stored salt from hex to bytes
        
        # Hash the provided password with the stored salt and compare
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)
        if hashed_password == stored_password:
            return True  # Return True if passwords match
        else:
            return False  # Return False if passwords do not match
        return
    
    # Method to delete a customer by customer ID
    def delete_customer(self, customer_id: int):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM customer WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))  # Execute delete query for the given customer ID
        self.db_connection.commit()  # Commit the changes to the database

    # Method to update the number of orders for a customer
    def update_number_orders(self, customer_id: int, number_orders: int):
        cursor = self.db_connection.cursor()
        query = "UPDATE customer SET number_orders = %s WHERE customer_id = %s"
        cursor.execute(query, (number_orders, customer_id))  # Update the number of orders for the given customer ID
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor

    # Method to get customer details by customer ID
    def get_customer_by_id(self, id: int) -> dict:
        cursor = self.db_connection.cursor()
        query = """
            SELECT c.name, c.last_name, ca.house_number, ca.apartment_number, pc.postal_code
            FROM customer c
            JOIN customer_address ca ON c.address = ca.customer_address_id
            JOIN postal_codes pc ON ca.postal_code_id = pc.ID
            WHERE c.customer_id = %s
        """
        cursor.execute(query, (id,))  # Execute query with the given customer ID
        result = cursor.fetchone()  # Fetch one result from the executed query
        cursor.close()  # Close the cursor

        # Return customer details in dictionary format if found
        if result:
            return {
                'name': result[0],
                'last_name': result[1],
                'address': f"{result[2]}, {result[3]} - {result[4]}"
            }
        return None  # Return None if customer not found