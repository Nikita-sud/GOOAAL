from datetime import datetime
from backend.repositories.customers.customer_intfc import CustomerInterface
import os
import hashlib

from backend.repositories.restaurants.restaurants_intfc import RestaurantsInterface

class RestaurantsRepo(RestaurantsInterface):
    
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def update_restaurant(self,customer_postal_code, new_order_price):
        cursor = self.db_connection.cursor()
        restaurant_id = 1
        if (customer_postal_code>=81):
            restaurant_id = 5
        elif (customer_postal_code<=80 and customer_postal_code>=61):
            restaurant_id=4
        elif (customer_postal_code<=60 and customer_postal_code>=41):
            restaurant_id=3
        elif (customer_postal_code<=40 and customer_postal_code>=21):
            restaurant_id=2
        elif (customer_postal_code<=20 and customer_postal_code>=1):
            restaurant_id=1

        query = """UPDATE restaurants
        SET earnings = earnings + %s
        WHERE restaurant_id = %s"""

        cursor.execute(query, (new_order_price, restaurant_id))
        self.db_connection.commit()

        cursor.close()
        print('Restaurant earnings was updated')
        return


    def add_earnings(self, new_order_price: float, customer_id:int):
        cursor = self.db_connection.cursor()
        query = """SELECT p.ID
        FROM customer AS c
        JOIN customer_address AS ca ON c.address = ca.customer_address_id
        JOIN postal_codes AS p ON ca.postal_code_id = p.ID
        WHERE c.customer_id = %s"""
        cursor.execute(query, (customer_id,))
        customer_postal_code = cursor.fetchone()
        cursor.close()
        self.update_restaurant(customer_postal_code[0], new_order_price)
        return
