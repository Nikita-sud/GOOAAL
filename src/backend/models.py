from src.backend.database import connect_to_db

def add_order(customer_id, pizza_id, status="processing"):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "INSERT INTO orders (customer_id, pizza_id, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (customer_id, pizza_id, status))
    connection.commit()
    cursor.close()
    connection.close()