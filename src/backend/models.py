from src.backend.database import connect_to_db

def add_order(customer_id, pizza_id, username, password, status="processing"):
    connection = connect_to_db(username, password)  # Передача username и password
    cursor = connection.cursor()
    query = "INSERT INTO orders (customer_id, pizza_id, status1) VALUES (%s, %s, %s)"
    cursor.execute(query, (customer_id, pizza_id, status))
    connection.commit()
    cursor.close()
    connection.close()