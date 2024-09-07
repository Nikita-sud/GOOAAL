import mysql.connector
from src.backend.ngrok_utils import get_ngrok_url  # Импорт функции для работы с ngrok

def connect_to_db(username, password):
    ngrok_url = get_ngrok_url()  # Попытка получить URL ngrok
    if ngrok_url:
        # Если ngrok доступен, используем его
        ngrok_host, ngrok_port = ngrok_url.replace("tcp://", "").split(":")
        print(f"Используется ngrok: {ngrok_host}:{ngrok_port}")
        connection = mysql.connector.connect(
            host=ngrok_host,
            port=int(ngrok_port),
            user=username,  # Используем введённый username
            password=password,  # Используем введённый password
            database="pizza_shop"
        )
    else:
        # Если ngrok недоступен, используем localhost
        print("ngrok недоступен, используется localhost")
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user=username,  # Используем введённый username
            password=password,  # Используем введённый password
            database="pizza_shop"
        )
    return connection