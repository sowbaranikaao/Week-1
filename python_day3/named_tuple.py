from typing import NamedTuple
class Student(NamedTuple):
    name:str
    age:int
    department:str
student = Student("Alice",20,"ECE")
print(student.department)