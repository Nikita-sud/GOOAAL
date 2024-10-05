# employee_repo.py

class EmployeeRepo():
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Method to check if an employee exists with the given email and password
    def check_employee(self, email, password):
        cursor = self.db_connection.cursor()
        query = """
        SELECT email, password
        FROM employee_credentials
        WHERE email = %s
        """
        cursor.execute(query, (email,))  # Execute query with the given email
        result = cursor.fetchone()  # Fetch one result from the executed query
        cursor.close()  # Close the cursor
        
        # Check if result is None (no matching email found) or if credentials match
        if result is None:
            return False  # Return False if no employee found
        elif result[0] == email and result[1] == password:
            return True  # Return True if email and password match
        return False  # Default return False if credentials do not match