from dataclasses import dataclass
@dataclass
class Student:
    name:str
    age:int=21
student=Student("John")
print(student)
print(student.name)
print(student.age)