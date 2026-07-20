from student_app import Student
from student_app import add_student
from student_app import get_students
from student_app import save_students
from student_app import display_students
student1=Student("Alice",20)
student2=Student("Bob",21)
add_student(student1)
add_student(student2)
students=get_students()
display_students(students)
save_students()