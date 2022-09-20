class Student:
    students = []
    announcements = []

    def __init__(self):
        pass



print("Welcome to Student Management System!")
print("""You can choose one of these functions:
List students
Add student
Search student
Assign grade
Add and view announcement
Delete student""")

command = ''
while command == "Log out":
    command = input("Enter your command: ").lower()