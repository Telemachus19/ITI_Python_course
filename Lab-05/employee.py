import sqlite3
from db import DB_PATH

class Employee:
    # Static list contains all employee
    all_employees = []

    def __init__(self, First_name, Last_name, Age, Department, Salary, db_id=None, save_to_db=True):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
        self.Department = Department
        self.Salary = Salary
        self.db_id = db_id

        # Insert the created object to the list
        Employee.all_employees.append(self)

        # Insert new record in table employee in database
        if save_to_db:
            self._insert_into_db()

    def _insert_into_db(self):
        """Helper to insert employee record into the database."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employee (first_name, last_name, age, department, salary, is_manager, managed_department)
            VALUES (?, ?, ?, ?, ?, 0, NULL)
        ''', (self.First_name, self.Last_name, self.Age, self.Department, self.Salary))
        conn.commit()
        self.db_id = cursor.lastrowid
        conn.close()

    def transfer(self, new_department):
        """Change employee department and update database record."""
        self.Department = new_department
        if self.db_id is not None:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE employee
                SET department = ?
                WHERE id = ?
            ''', (new_department, self.db_id))
            conn.commit()
            conn.close()

    def fire(self):
        """Remove the employee from the shared list and delete database record."""
        if self in Employee.all_employees:
            Employee.all_employees.remove(self)
        
        if self.db_id is not None:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM employee
                WHERE id = ?
            ''', (self.db_id,))
            conn.commit()
            conn.close()

    def show(self):
        """Prints all employee data."""
        print(f"\n--- Employee Profile (ID: {self.db_id}) ---")
        print(f"First Name: {self.First_name}")
        print(f"Last Name: {self.Last_name}")
        print(f"Age: {self.Age}")
        print(f"Department: {self.Department}")
        print(f"Salary: {self.Salary}")
        print("----------------------------------")

    @classmethod
    def List_employees(cls):
        """Select all employees and print their data."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT id, first_name, last_name, age, department, salary, is_manager, managed_department FROM employee')
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("\nNo employees found in the database.\n")
            return

        print("\n--- EMPLOYEES LIST ---")
        for row in rows:
            db_id, first_name, last_name, age, department, salary, is_manager, managed_department = row
            if is_manager:
                print(f"[Manager] ID: {db_id:<3} | Name: {first_name} {last_name:<15} | Age: {age:<3} | Dept: {department:<12} | Managed Dept: {managed_department:<12} | Salary: confidential")
            else:
                print(f"[Employee] ID: {db_id:<3} | Name: {first_name} {last_name:<15} | Age: {age:<3} | Dept: {department:<12} | Salary: {salary:<10}")
        print("----------------------\n")
