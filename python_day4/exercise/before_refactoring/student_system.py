students=[]
def add_student(name,age):
    student={
        "name":name,
        "age":age
    }
    students.append(student)
def display_student():
    print("\nStudent List")
    print("-----------------")
    for student in students:
        print(f"Name : {student['name']}")
        print(f"Age : {student['age']}")
        print()
def save_students():
    print("Students saved successfully")
def main():
    add_student("Alice",20)
    add_student("Bob",21)
    display_student()
    save_students()
main()

