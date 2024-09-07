import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",        # Хост вашего сервера MySQL
        user="your_user",        # Ваш пользователь MySQL
        password="your_password",# Пароль пользователя MySQL
        database="pizza_shop"    # Ваша база данных
    )
    return connection