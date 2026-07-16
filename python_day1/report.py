employees = ["John", "Alice", "Sam"]
salary = [50000, 60000, 70000]
with open("salary.txt","w") as file:
    for emp,sal in zip(employees,salary):
        file.write(f"{emp}:{sal}\n")
print("File created")
