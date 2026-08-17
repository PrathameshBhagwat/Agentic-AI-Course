# 3. Create a simple Employee Management System using Class and Object in Python.
# What to Do
# 1. Create a class named Employee.
# 2. Create a constructor __init__() to initialize:
# o Employee name
# o Employee ID
# o Department
# o Basic salary
# 3. Create a display_details() method to display employee information.
# 4. Create a calculate_salary() method:
# o Add a fixed bonus of ₹5,000.
# o Calculate and display the final salary.
# 5. Create a check_salary() method:
# o If salary is ₹30,000 or above, display "Good Salary".
# o Otherwise, display "Average Salary".
# 6. Create a menu-driven program:
# o 1 → Display Details
# o 2 → Calculate Salary
# o 3 → Check Salary
# o 4 → Exit

class Employee:
    def __init__(self,employee_id,employee_name,department,basic_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.basic_salary = basic_salary
        self.final_salary = 0
        
    def display_employee(self):
        print("Employee ID : ",self.employee_id)
        print("Employee Name : ", self.employee_name)
        print("Employee Department : ", self.department)
        print("Employee Salary (With Bonus) : ",self.final_salary)

    def calculate_salary(self):
        self.final_salary=self.basic_salary+5000
        print("Salary after the bonus : ",self.final_salary)

    def check_salary(self):
        if self.final_salary>30000:
            print("Good Salary : ", self.final_salary)
        else:
            print("Average Salary : ",self.final_salary)
        
        
        
def add_employee():
    employee_id =int(input("Enter the Employee id : "))
    if employee_id in employees:
        print("The employee is already in the company")
        return
        
    employee_name  =input("Enter the Employee name : ")
    department = input("Enter your department : ")
    basic_salary = float(input("Enter your basic salary : "))
        
    employee = Employee(employee_id,employee_name,department,basic_salary)
        
    employees[employee_id]= employee
        
    print("Employee added successfully.")

def display_details():
    input_id = int(input("Enter the Employee ID : "))
        
    if input_id in employees:
        employee = employees[input_id]
            
        employee.display_employee()
        
    else:
        print("Employee not found.")

def cal_salary():
    input_id = int(input("Enter the Employee ID : "))
    
    if input_id in employees:
        employee = employees[input_id]
        employee.calculate_salary()
    else:
        print("Employee not found")

def check_salary():
    input_id = int(input("Enter the Employee ID : "))
        
    if input_id in employees:
        employee = employees[input_id]
            
        employee.check_salary()
        
    else:
        print("Employee not found.")

employees = {}

while True:
    print("1. Add Employee")
    print("2. Display employee details")
    print("3. Calculate Salary")
    print("4. Check Salary")
    print("5. Exit")
        
    choice = int(input("Enter your choice : "))
        
    match choice:
        case 1:
            add_employee()
            
        case 2:
            display_details()
                
        case 3:
            cal_salary()
                
        case 4:
            check_salary()
        
        case 5:
            print("Thank you")
            break
        
        case _:
            print("Invalid Choice.")
