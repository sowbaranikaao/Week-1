class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Cat(Animal):
    def meow(self):
        print("Meowing...")

dog = Dog()
dog.breathe()
dog.bark()

cat = Cat()
cat.breathe()
cat.meow()