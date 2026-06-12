import sqlite3
from db import DB_PATH
from employee import Employee

class Manager(Employee):
    def __init__(self, First_name, Last_name, Age, Department, Salary, Managed_department, db_id=None, save_to_db=True):
        self.Managed_department = Managed_department
        # Call constructor of parent class but bypass direct db save
        super().__init__(First_name, Last_name, Age, Department, Salary, db_id=db_id, save_to_db=False)
        
        if save_to_db:
            self._insert_into_db()

    def _insert_into_db(self):
        """Helper to insert manager record into the database."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employee (first_name, last_name, age, department, salary, is_manager, managed_department)
            VALUES (?, ?, ?, ?, ?, 1, ?)
        ''', (self.First_name, self.Last_name, self.Age, self.Department, self.Salary, self.Managed_department))
        conn.commit()
        self.db_id = cursor.lastrowid
        conn.close()

    def show(self):
        """Prints all manager data except salary is hidden as confidential."""
        print(f"\n~~~ Manager Profile (ID: {self.db_id}) ~~~")
        print(f"First Name: {self.First_name}")
        print(f"Last Name: {self.Last_name}")
        print(f"Age: {self.Age}")
        print(f"Department: {self.Department}")
        print(f"Managed Department: {self.Managed_department}")
        print("Salary: confidential")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
