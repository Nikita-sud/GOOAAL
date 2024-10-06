import sys
import os
# Add the project root directory to the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from mysql.connector import Error
from src.backend.database import connect_to_db

def generate_earnings_report(connection, month, year, postal_code=None, city=None, gender=None, age_from=None, age_to=None):
    try:
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            # Build the base query with dynamic age calculation
            query = """
            SELECT
                IFNULL(SUM(o.total_price), 0) AS total_earnings,
                IFNULL(COUNT(o.order_id), 0) AS total_orders
            FROM orders o
            JOIN customer c ON o.customer_id = c.customer_id
            JOIN gender g ON c.gender_id = g.gender_id
            JOIN customer_address ca ON c.address = ca.customer_address_id
            JOIN postal_codes pc ON ca.postal_code_id = pc.ID
            JOIN cities ci ON ca.city_id = ci.ID
            WHERE MONTH(o.created_at) = %s AND YEAR(o.created_at) = %s
            """
            params = [month, year]
            # Add filters based on the provided parameters
            if postal_code:
                query += " AND pc.postal_code = %s"
                params.append(postal_code)
            if city:
                query += " AND ci.City = %s"
                params.append(city)
            if gender:
                query += " AND g.gender = %s"
                params.append(gender)
            if age_from is not None and age_to is not None:
                query += """
                AND ((YEAR(CURDATE()) - YEAR(c.birthdate)) - 
                (DATE_FORMAT(CURDATE(), '%%m%%d') < DATE_FORMAT(c.birthdate, '%%m%%d'))) BETWEEN %s AND %s
                """
                params.extend([age_from, age_to])
            elif age_from is not None:
                query += """
                AND ((YEAR(CURDATE()) - YEAR(c.birthdate)) - 
                (DATE_FORMAT(CURDATE(), '%%m%%d') < DATE_FORMAT(c.birthdate, '%%m%%d'))) >= %s
                """
                params.append(age_from)
            elif age_to is not None:
                query += """
                AND ((YEAR(CURDATE()) - YEAR(c.birthdate)) - 
                (DATE_FORMAT(CURDATE(), '%%m%%d') < DATE_FORMAT(c.birthdate, '%%m%%d'))) <= %s
                """
                params.append(age_to)
            # Execute the query
            cursor.execute(query, params)
            result = cursor.fetchone()
            total_earnings = result['total_earnings']
            total_orders = result['total_orders']
            # Prepare the report content
            report_content = f"""Monthly Earnings Report
---------------------------
Month: {month}
Year: {year}
Total Earnings: €{total_earnings:.2f}
Total Orders: {total_orders}

Filters Applied:
"""
            if postal_code:
                report_content += f"- Postal Code: {postal_code}\n"
            if city:
                report_content += f"- City: {city}\n"
            if gender:
                report_content += f"- Gender: {gender}\n"
            if age_from is not None and age_to is not None:
                report_content += f"- Age Between: {age_from} and {age_to}\n"
            elif age_from is not None:
                report_content += f"- Age From: {age_from}\n"
            elif age_to is not None:
                report_content += f"- Age To: {age_to}\n"
            # Ensure the reports directory exists
            script_dir = os.path.dirname(os.path.abspath(__file__))
            reports_dir = os.path.join(script_dir, '..', 'reports')
            reports_dir = os.path.abspath(reports_dir)
            os.makedirs(reports_dir, exist_ok=True)
            # Save the report to a file
            report_filename = f"earnings_report_{year}_{month}.txt"
            report_path = os.path.join(reports_dir, report_filename)
            with open(report_path, 'w') as file:
                file.write(report_content)
            print(f"Report saved to {report_path}")
        else:
            print("Failed to connect to the database.")
    except Error as e:
        print(f"Error while executing the query: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    connection = connect_to_db()
    try:
        generate_earnings_report(
            connection,
            month=10,
            year=2024,
            postal_code='6211CL',
            city='Maastricht',
            gender='M',
            age_from=0,
            age_to=200
        )
    finally:
        if connection.is_connected():
            connection.close()