import sys

from db import init_db
from employee import Employee
from manager import Manager
from utils import load_employees_from_db, find_employee_by_id, show_menu

def main():
    init_db()
    load_employees_from_db()
    
    while True:
        show_menu()
        choice = input("Enter keyword: ").strip().lower()
        
        if choice == 'add':
            print("If manager press \"m\"/ if employee press 'e'")
            type_choice = input(">> ").strip().lower()
            if type_choice not in ['m', 'e']:
                print("Invalid type selection. Operation cancelled.")
                continue
                
            print("Please insert data")
            name = input("Name:>> ").strip()
            name_parts = name.split(maxsplit=1)
            first_name = name_parts[0] if len(name_parts) > 0 else "Unknown"
            last_name = name_parts[1] if len(name_parts) > 1 else ""
            
            try:
                age = int(input("Age:>> ").strip())
            except ValueError:
                print("Age must be an integer. Operation cancelled.")
                continue
                
            department = input("Department:>> ").strip()
            
            try:
                salary = float(input("Salary:>> ").strip())
            except ValueError:
                print("Salary must be a number. Operation cancelled.")
                continue
            
            if type_choice == 'm':
                managed_department = input("Managed Department:>> ").strip()
                mgr = Manager(
                    First_name=first_name,
                    Last_name=last_name,
                    Age=age,
                    Department=department,
                    Salary=salary,
                    Managed_department=managed_department
                )
                print(f"Manager {first_name} {last_name} added successfully (ID: {mgr.db_id})!")
            else:
                emp = Employee(
                    First_name=first_name,
                    Last_name=last_name,
                    Age=age,
                    Department=department,
                    Salary=salary
                )
                print(f"Employee {first_name} {last_name} added successfully (ID: {emp.db_id})!")
                
        elif choice == 'list':
            Employee.List_employees()
            
        elif choice == 'show':
            try:
                emp_id = int(input("Enter employee/manager ID to show: ").strip())
            except ValueError:
                print("ID must be an integer.")
                continue
            
            emp = find_employee_by_id(emp_id)
            if emp:
                emp.show()
            else:
                print(f"No employee/manager found with ID {emp_id}.")
                
        elif choice == 'transfer':
            try:
                emp_id = int(input("Enter employee/manager ID to transfer: ").strip())
            except ValueError:
                print("ID must be an integer.")
                continue
            
            emp = find_employee_by_id(emp_id)
            if emp:
                new_dept = input("Enter new department: ").strip()
                if new_dept:
                    emp.transfer(new_dept)
                    print(f"Transferred {emp.First_name} {emp.Last_name} to {new_dept} successfully!")
                else:
                    print("Department name cannot be empty.")
            else:
                print(f"No employee/manager found with ID {emp_id}.")
                
        elif choice == 'fire':
            try:
                emp_id = int(input("Enter employee/manager ID to fire: ").strip())
            except ValueError:
                print("ID must be an integer.")
                continue
                
            emp = find_employee_by_id(emp_id)
            if emp:
                name = f"{emp.First_name} {emp.Last_name}"
                emp.fire()
                print(f"Fired {name} (ID: {emp_id}) successfully!")
            else:
                print(f"No employee/manager found with ID {emp_id}.")
                
        elif choice == 'q':
            print("Exiting program. Goodbye!")
            sys.exit(0)
            
        else:
            print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()
