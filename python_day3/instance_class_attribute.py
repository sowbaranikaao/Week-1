class Student:
    college="KEC"
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Dummy:
    s1=Student("John",20)
    s2=Student("Alice",22)
    print(f"{s1.name} is {s1.age} years old.")
    print(s1.college)
    print(f"{s2.name} is {s2.age} years old.")
    print(s2.college)