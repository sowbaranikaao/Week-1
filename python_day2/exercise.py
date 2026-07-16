"""
def register_employee(name, age, salary, department):

    if name == "":
        print("Invalid Name")
        return

    if age < 18:
        print("Employee must be above 18")
        return

    if salary < 0:
        print("Salary cannot be negative")
        return

    if department == "":
        print("Department is required")
        return

    tax = salary * 0.10
    bonus = salary * 0.05
    final_salary = salary - tax + bonus

    print("Employee Details")
    print("---------------------")
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)
    print("Salary:", salary)
    print("Tax:", tax)
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)

    print("Saving employee...")

    print("Employee saved successfully.")

    print("Sending welcome email...")

    print("Email sent successfully.")

    print("Generating employee ID...")

    employee_id = name[:3].upper() + str(age)

    print("Employee ID:", employee_id)

    print("Registration Completed")
"""

def validate_name(name:str)->bool:
    """
    Validate the name of employee
    """
    return bool(name.strip())
def validate_age(age:int)->bool:
    """
    Validate the age of employee"""
    return age>18
def validate_salary(salary:float)->bool:
    """
    Validate the salary of employee"""
    return salary>0
def validate_department(department:str)->bool:
    """
    Validate the department of employee"""
    return bool(department.strip())
def calculate_tax(salary:float)->float:
    """
    Calculate tax for the employee"""
    return salary*0.10
def calculate_bonus(salary:float)->float:
    """
    Calculate bonus for the employee"""
    return salary*0.05
def calculate_final_salary(salary:float)->float:
    """
    Calculate final salary for the employee"""
    tax=calculate_tax(salary)
    bonus=calculate_bonus(salary)
    return salary-tax+bonus
def display_employee_details(name:str,age:int,department:str,salary:float,final_salary:float):
    """
    Display employee details"""
    print("Employee Details")
    print("---------------------")
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)
    print("Salary:", salary)
    print("Final Salary:", final_salary)
def decorator1(func):
    def wrapper(name:str):
        print("Saving employee...")
        func(name)
        print("Employee saved successfully.")
    return wrapper
@decorator1
def save_employee(name:str):
    """
    Save employee details"""
    print(f"{name} saved successfully.")
def decorator2(func):
    def wrapper(name:str):
        print("Sending welcome email...")
        func(name)
        print("Email sent successfully.")
    return wrapper
@decorator2
def send_email(name:str):
    """
        Send welcome email to employee"""
    print(f"Welcome email sent to {name}.")
def generate_emp_id(name:str,age:int):
    """
    Generate employee ID"""
    return name[:3].upper()+str(age)
def print_emp_id(emp_id:str):
    """
    Print employee ID"""
    print("Employee ID:",emp_id)
def register_employee(name:str,age:int,salary:float,department:str):
    """
    Register new employee with given details"""
    if not validate_name(name):
        print("Invalid Name")
        return
    if not validate_age(age):
        print("Employee must be above 18")
        return 
    if not validate_salary(salary):
        print("Salary cannot be negative")
        return
    if not validate_department(department):
        print("Department is required")
        return
    tax=calculate_tax(salary)
    bonus=calculate_bonus(salary)
    final_salary=calculate_final_salary(salary)
    display_employee_details(name,age,department,salary,final_salary)
    save_employee(name)
    send_email(name)
    emp_id=generate_emp_id(name,age)
    print_emp_id(emp_id)
    print("Registration Completed")

register_employee("Sow", 21, 50000, "ECE")


