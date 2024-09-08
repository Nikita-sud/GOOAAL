from src.backend.database import connect_to_db

def add_order(customer_id, pizza_id, username, password, status="processing"):
    connection = connect_to_db(username, password)  # Передача username и password
    cursor = connection.cursor()
    query = "INSERT INTO orders (customer_id, pizza_id, status1) VALUES (%s, %s, %s)"
    cursor.execute(query, (customer_id, pizza_id, status))
    connection.commit()
    cursor.close()
    connection.close()

def verify_user_credentials(username, password):
    connection = None
    try:
        connection = connect_to_db(username, password)
        cursor = connection.cursor()
        
        # Query to check if the username exists in the users table
        query = "SELECT COUNT(*) FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        # If user exists and password is correct, return True
        if result and result[0] > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error verifying user: {e}")
        return False
    finally:
        if connection:
            connection.close()