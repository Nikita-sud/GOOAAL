import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="Nichita",
        password="28082004", 
        database="pizza_shop"
    )
    return connection