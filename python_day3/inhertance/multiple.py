class A:
    def show(self):
        print("A class show method")
class B:
    def show(self):
        print("B class show method")
class C(A,B):
    pass    
class Dummy:
    c=C()
    c.show()