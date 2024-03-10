import Employee
import db

def menu():
    print("Welcome To Your Employee Management System \n")
    print("1.Add Employee")
    print("2.List Employees")
    print("3.Update Employee")
    print("4.Delete Employee")
    print("5.Exit")
    choice = input("Selection: ")
    return choice

def addEmployee(ems):
    print("Enter Employee Details: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    emp_id = int(input("Employee ID: "))
    date_of_emp = input("Date of Employment (YYYY-MM-DD): ")
    salary = float(input("Salary: "))
    department = input("Department: ")
    empl = Employee.Employees(first_name, last_name, emp_id, date_of_emp, salary, department)
    ems.add_employee(empl)

def udpateEmployee(ems):
    emp_id = int(input("Enter Employee ID You Wish To Update: "))
    employee = ems.emp_by_id(emp_id)
    if(employee):
        print("Enter New Employee Details: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        date_of_emp = input("Date of Employment (YYYY-MM-DD): ")
        salary = float(input("Salary: "))
        department = input("Department: ")
        ems.update_emp(emp_id,first_name=first_name,last_name=last_name,date_of_emp=date_of_emp,salary=salary,department=department)
    else:
        print(f"Employee ID [{emp_id}] Not Found.")

def deleteEmployee(ems):
    emp_id = int(input("Enter Employee ID To Delete: "))
    if(ems.delete_emp(emp_id)):
        print("Employee Deleted. ")
    else:
        print(f"Employee Not Found With ID: {emp_id}")

def listEmployee(ems):
    ems.list_emp()

def main():
    ems = Employee.EmployeeMS()
    
    while True:
        choice = menu()
        if choice == '1':
            addEmployee(ems)
        elif choice == '2':
            listEmployee(ems)
        elif choice == '3':
            udpateEmployee(ems)
        elif choice == '4':
            deleteEmployee(ems)
        elif choice == '5':
            print(".....GoodBye.....")
            break
        else:
            print("Invalid input. Try again.")