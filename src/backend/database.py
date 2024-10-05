# database.py

import mysql.connector

# Function to establish a connection to the database
def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",  # Host address of the database server
        port=3306,  # Port number for MySQL server
        user="admin",  # Username for the database
        password="12345",  # Password for the database
        database="test_pizza_shop",  # Name of the database to connect to
        autocommit=True
    )
    return connection  # Return the database connection object