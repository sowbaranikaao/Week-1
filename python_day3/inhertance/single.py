class A:
    def show(self):
        print("A class show method")
class B(A):
    def show(self):
        super().show()
        print("B class show method")
class Dummy():
    b=B()
    b.show()