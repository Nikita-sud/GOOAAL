import os
import mysql.connector
import subprocess


def clean_sql_script(script):
    cleaned_script = []
    for line in script.splitlines():
        if not line.strip().startswith('--') and not line.strip().startswith('#') and line.strip():
            cleaned_script.append(line)
    return ' '.join(cleaned_script)

def download_db():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",  
            password="12345",  
            port=3306
        )

        cursor = connection.cursor()

        cursor.execute("DROP DATABASE IF EXISTS test_pizza_shop")
        connection.commit()

        cursor.execute("CREATE DATABASE test_pizza_shop")
        connection.commit()

        cursor.execute("USE test_pizza_shop")

        with open(fr"database\test_pizza_shop.sql", "r") as sql_file:
            sql_script = sql_file.read()

        cleaned_sql = clean_sql_script(sql_script)

        for statement in cleaned_sql.split(";"):
            if (statement.strip()):
                for result in cursor.execute(statement, multi=True):
                    pass

        cursor.execute("SHOW FULL TABLES;")
        all_tables = cursor.fetchall()
        for table in all_tables:
            print(table)

        cursor.close()
        connection.close()
        print("DB was LOADED")

    except Exception as ex:
        print("CONNECTION FAILED: "+str(ex))
        pass


def upload_db():
    try:
        username = "root"  
        password = "12345"  
        database = "test_pizza_shop"  
        
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        output_folder = os.path.join(current_dir, "database") 
        sql_file = os.path.join(output_folder,"..", "..","..","database", "test_pizza_shop.sql")

        command = fr"mysqldump -u {username} -p{password} {database} > {sql_file}"
        subprocess.run(command, shell=True, check=True)


    except Exception as ex:
        print("FAILED ON UPLOADING "+ str(ex))

download_db()
upload_db()