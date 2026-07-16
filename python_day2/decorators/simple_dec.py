def decorator(func):
    def wrapper():
        print("Program started")
        func()
        print("Program ended")
    return wrapper

@decorator
def display():
    print("Hello World")
display()