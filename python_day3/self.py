class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Dummy:
    s1=Student("John",20)
    s1.display()
    s2=Student("Alice",22)
    s2.display()