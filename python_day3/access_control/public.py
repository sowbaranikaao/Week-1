class Employee:
    def __init__(self):
        self.salary=10000
class Dummy():
    emp=Employee()
    emp.salary=-10
    print(emp.salary)
