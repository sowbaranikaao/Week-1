class Employee:
    def __init__(self):
        self.__salary=10000
class Dummy():
    emp=Employee()
    print(emp._Employee__salary)
    print(emp.__salary)
