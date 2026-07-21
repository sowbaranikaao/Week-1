class InvalidAgeError(Exception):
    pass
try:
    age=int(input("Enter age: "))
    if age<=0:
        raise InvalidAgeError("Age cant be negative")
    print("Age : ",age)
except InvalidAgeError as error:
    print(error)
except ValueError:
    print("Please enter numbers only")
