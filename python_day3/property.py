class Employee:
    def __init__(self,salary):
        self._salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value<0:
            print("Invalid salary")
        else:
            self._salary=value
    @salary.deleter
    def salary(self):
        print("Salary Deleted")
        del self._salary
class Dummy():
    emp=Employee(10000)
    emp.salary=20000
    print(emp.salary)
    emp.salary=-10
    print(emp.salary)