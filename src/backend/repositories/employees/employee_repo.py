class EmployeeRepo():
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def check_employee(self,email, password):
        cursor = self.db_connection.cursor()
        query = """
        SELECT email, password
        FROM employee_credentials
        WHERE email = %s
        """
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        if(result == None):
            return False
        elif(result[0]==email and result[1]==password):
            return True