from python_day4.school.database import save_student
def add_student(name):
    if len(name)<3:
        print("Invalid name")
        return
    save_student(name)