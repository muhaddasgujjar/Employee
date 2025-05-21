import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_user",
        password="your_pass",
        database="employee_db"
    )
