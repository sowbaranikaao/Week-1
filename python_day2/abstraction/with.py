def calculate(salary):
    tax = salary * 0.1
    bonus = salary * 0.05
    final_salary = salary - tax + bonus
    return final_salary
print(calculate(50000))