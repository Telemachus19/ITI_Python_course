import os
import sqlite3
from db import DB_PATH
from employee import Employee
from manager import Manager

def load_employees_from_db():
    """Loads all records from the database into the shared memory list."""
    Employee.all_employees.clear()
    if not os.path.exists(DB_PATH):
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, first_name, last_name, age, department, salary, is_manager, managed_department FROM employee')
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        db_id, first_name, last_name, age, department, salary, is_manager, managed_department = row
        if is_manager:
            Manager(
                First_name=first_name,
                Last_name=last_name,
                Age=age,
                Department=department,
                Salary=salary,
                Managed_department=managed_department,
                db_id=db_id,
                save_to_db=False
            )
        else:
            Employee(
                First_name=first_name,
                Last_name=last_name,
                Age=age,
                Department=department,
                Salary=salary,
                db_id=db_id,
                save_to_db=False
            )


def find_employee_by_id(db_id):
    """Finds an employee or manager in the shared list by their DB ID."""
    for emp in Employee.all_employees:
        if emp.db_id == db_id:
            return emp
    return None


def show_menu():
    """Prints the operation menu for the CLI."""
    print("\n--- MENU ---")
    print("add      - Add a new Employee or Manager")
    print("list     - List all employees/managers")
    print("show     - Show details of an employee/manager")
    print("transfer - Transfer an employee/manager to another department")
    print("fire     - Fire an employee/manager")
    print("q        - Exit the program")
    print("------------")
