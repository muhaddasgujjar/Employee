import mysql.connector

# Shared function to get a database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employee"
    )
# This file can be left empty, or used to expose key modules

# Example: exposing functions from different modules


from app.views.attendance_ui import open_attendance_ui
from app.views.leave_ui import open_leave_ui
from app.views.payroll_ui import  open_payroll_ui
from app.views.department_ui  import open_department_ui
from app.views.performance_ui import  open_performance_ui



