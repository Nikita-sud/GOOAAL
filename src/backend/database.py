import mysql.connector
from src.backend.ngrok_utils import get_ngrok_url  # Импорт функции для работы с ngrok

def connect_to_db():
    
    ngrok_url = get_ngrok_url()  
    if ngrok_url:
        ngrok_host, ngrok_port = ngrok_url.replace("tcp://", "").split(":")
        print(f"Используется ngrok: {ngrok_host}:{ngrok_port}")
        connection = mysql.connector.connect(
            host=ngrok_host,
            port=int(ngrok_port),
            user="root",  
            password="12345",  
            database="test_pizza_shop"
        )
    else:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",  
            password="12345",  
            database="test_pizza_shop"
        )
    return connection