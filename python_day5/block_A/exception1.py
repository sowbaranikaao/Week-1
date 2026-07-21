def calculation():
    try:
        num1=int(input("Enter number1 :"))
        num2=int(input("Enter number2 :"))
    except ValueError as err1:
        print("Invalid numbers")
    try:
        ans=num1/num2
    except ZeroDivisionError as err2:
        print(err2)
    else:
        print(ans)
        print("Division successful")
calculation() 
    
        
