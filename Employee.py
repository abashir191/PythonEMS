import datetime
import json
import Main

class Employees:
    def __init__(self, first_name, last_name, emp_id, date_of_emp, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_id = emp_id
        self.date_of_emp = date_of_emp
        self.salary = salary
        self.department = department

class Department:
    def __init__(self,dep_name):
        self.dep_name = dep_name

class EmployeeMS:
    def __init__(self):
        self.employees_list = []
        
    def add_employee(self, employee):
        if self.emp_by_id(employee.emp_id):
            print("Change ID to a different value")
            return False
        self.employees_list.append(employee)
        print("employee successfully added")
        return True

    def emp_by_id(self, emp_id):
        for emp in self.employees_list:
            if emp.emp_id == emp_id:
                return emp
        return None

    def update_emp(self,emp_id, **kwargs):
        emp = self.emp_by_id(emp_id)
        if emp:
            for key, value in kwargs.items():
                setattr(emp, key, value)
            print("Employee updated successfully.")
        else:
            print(f"Employee ID[{emp_id}] not found.")
    def delete_emp(self,emp_id):
        for emp in self.employees_list:
            if emp.emp_id == emp_id:
                self.employees_list.remove(emp)
                print(f"Employee with ID [{emp_id}] successfully removed.")
                return True
        print("Employee not found.")
        return False

    def list_emp(self):
        #List Comprehension
        emp_ids = [(emp.emp_id, emp.first_name, emp.last_name, emp.date_of_emp, emp.salary, emp.department) for emp in self.employees_list]
        if not emp_ids:
            print("No employees found")
        else:
            print("Employees:")
            print("--------------------------------")
            for emp_id, first_name, last_name, date_of_emp, salary, department in emp_ids:
                print("Id: ", emp_id)
                print("Name: ", first_name, last_name)
                print("Date of Employment: ", date_of_emp)
                print("Salary : ", salary)
                print("Department : ", department)
                print("--------------------------------")

if __name__ == '__main__' :
    Main.main()