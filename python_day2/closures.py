def outer():
    msg="Hello"
    def inner():
        print(msg)
    return inner
greet=outer()
greet()