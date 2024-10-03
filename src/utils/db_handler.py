import os
import mysql.connector
import subprocess

def clean_sql_script(script):
    cleaned_script = []
    for line in script.splitlines():
        if not line.strip().startswith('--') and not line.strip().startswith('#') and line.strip():
            if "DELIMITER" not in line:
                cleaned_script.append(line.strip())
    return ' '.join(cleaned_script)

def sync_db():
    try:
        username = "admin"
        password = "12345"
        database = "test_pizza_shop"
        sql_file_path = os.path.join("database", "test_pizza_shop.sql")
        
        command = f"mysql -u {username} -p{password} {database} < {sql_file_path}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode != 0:
            print(f"Error syncing DB: {result.stderr.decode()}")
        else:
            print("Database synced successfully")
    
    except Exception as ex:
        print(f"Error during DB sync: {str(ex)}")

def download_db():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="admin",  
            password="12345",  
            port=3306
        )

        cursor = connection.cursor()

        cursor.execute("DROP DATABASE IF EXISTS test_pizza_shop")
        connection.commit()

        cursor.execute("CREATE DATABASE test_pizza_shop")
        connection.commit()

        cursor.execute("USE test_pizza_shop")

        with open(fr"database/test_pizza_shop.sql", "r", encoding="utf-8") as sql_file:
            sql_script = sql_file.read()

        cleaned_sql = clean_sql_script(sql_script)

        # Split SQL statements correctly and handle multi-statement execution
        sql_statements = cleaned_sql.split(";")
        for statement in sql_statements:
            if statement.strip():
                try:
                    print(f"Executing SQL statement: {statement.strip()}")  # Debugging
                    cursor.execute(statement)
                except mysql.connector.Error as err:
                    print(f"Error executing statement: {statement.strip()}")
                    print(f"MySQL Error: {err}")
                    break

        cursor.execute("SHOW FULL TABLES;")
        all_tables = cursor.fetchall()
        for table in all_tables:
            print(table)

        cursor.close()
        connection.close()
        print("DB was DOWNLOADED. You are using the latest version")

    except Exception as ex:
        print("CONNECTION FAILED: " + str(ex))
        pass

def upload_db():
    try:
        username = "admin"  
        password = "12345"  
        database = "test_pizza_shop"  
        
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        output_folder = os.path.abspath(os.path.join(current_dir, "..","..", "database"))
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        sql_file = os.path.join(output_folder, "test_pizza_shop.sql")

        print(f"SQL file path: {sql_file}")
        
        command = f"mysqldump -u {username} -p{password} {database} > {sql_file}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print(f"ERROR: {result.stderr.decode()}")
        else:
            print("DB was uploaded successfully")

    except Exception as ex:
        print(f"FAILED ON UPLOADING: {str(ex)}")

# upload_db()
# download_db()
