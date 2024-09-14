import mysql.connector
from src.backend.ngrok_utils import get_ngrok_url  # Импорт функции для работы с ngrok

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",  
        password="12345",  
        database="test_pizza_shop")
    return connection