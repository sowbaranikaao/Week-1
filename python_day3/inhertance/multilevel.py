class A:
    def show(self):
        print("A class show method")
class B(A):
    def display(self):
        print("B class display method")
class C(B):
    pass
class Dummy:
    c=C()
    c.show()
    c.display()