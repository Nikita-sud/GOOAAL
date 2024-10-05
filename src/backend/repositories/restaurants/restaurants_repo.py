# restaurants_repo.py

from datetime import datetime
from backend.repositories.customers.customer_intfc import CustomerInterface
import os
import hashlib

from backend.repositories.restaurants.restaurants_intfc import RestaurantsInterface

# Defining the RestaurantsRepo class that implements the RestaurantsInterface
class RestaurantsRepo(RestaurantsInterface):
    
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Method to update restaurant earnings based on customer postal code and new order price
    def update_restaurant(self, customer_postal_code, new_order_price):
        cursor = self.db_connection.cursor()
        
        # Determine the restaurant ID based on the postal code range
        restaurant_id = 1
        if customer_postal_code >= 81:
            restaurant_id = 5
        elif 61 <= customer_postal_code <= 80:
            restaurant_id = 4
        elif 41 <= customer_postal_code <= 60:
            restaurant_id = 3
        elif 21 <= customer_postal_code <= 40:
            restaurant_id = 2
        elif 1 <= customer_postal_code <= 20:
            restaurant_id = 1

        # Update the earnings for the determined restaurant
        query = """UPDATE restaurants
        SET earnings = earnings + %s
        WHERE restaurant_id = %s"""
        cursor.execute(query, (new_order_price, restaurant_id))
        self.db_connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
        print('Restaurant earnings was updated')
        return

    # Method to add earnings for a restaurant based on a new order
    def add_earnings(self, new_order_price: float, customer_id: int):
        cursor = self.db_connection.cursor()
        # Query to get the postal code ID of the customer
        query = """SELECT p.ID
        FROM customer AS c
        JOIN customer_address AS ca ON c.address = ca.customer_address_id
        JOIN postal_codes AS p ON ca.postal_code_id = p.ID
        WHERE c.customer_id = %s"""
        cursor.execute(query, (customer_id,))  # Execute query to get postal code ID of the customer
        customer_postal_code = cursor.fetchone()  # Fetch the postal code ID
        cursor.close()  # Close the cursor

        # Update restaurant earnings based on the customer's postal code
        self.update_restaurant(customer_postal_code[0], new_order_price)
        return