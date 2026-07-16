with open("students.txt") as file:
    for student in file:
        print(student.strip())
