emp_name=["Alice","Bob","John"]
salary=[50000,60000,70000]
with open("report.txt","w") as file:
    for index,(name,sal) in enumerate(zip(emp_name,salary),start=1):
        bonus=sal*0.1
        file.write(f"{index}. {name} Salary: {sal} Bonus: {bonus} Total: {sal+bonus}\n")
