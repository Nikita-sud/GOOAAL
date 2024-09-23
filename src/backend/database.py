# database.py
import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="admin",  
        password="12345",  
        database="test_pizza_shop")
    return connection