class A:
    def greet(self):
        print("A")
class GreetingMixin:
    def greet(self):
        print("Mixin")
        super().greet()
class B(GreetingMixin, A):
    pass
obj=B()
obj.greet()