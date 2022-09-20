class Student:
    students = []
    announcements = []

    def __init__(self):
        pass
    
    def add_student(self):
        self.name = input("Enter student's name: ").capitalize()
        self.surname = input("Enter student's surname: ").capitalize()
        self.fullname = self.name + " " + self.surname
        self.email = self.name.lower() + self.surname.lower() + "@gmail.com"
        if self.email in Student.students:
            self.email = self.name.lower() + self.surname.lower() + "2@gmail.com"
        Student.students.append(dict({"fullname": self.fullname, "email": self.email}))


print("Welcome to Student Management System!")
print("""You can choose one of these functions:
List students
Add student
Search student
Assign grade
Add and view announcement
Delete student""")

command = ""
while command == "Log out":
    command = input("Enter your command: ").lower()
    if command == "add student":
        std = Student()
        std.add_student()
        while input("Do you want to add new student? Y/N ").lower() == "y":
            std = Student()
            std.add_student()
        else:
            print("Students were added successfully!")

    elif command == "list students":
        if Student.students:
            for student in Student.students:
                print("Student's fullname: " + student["fullname"])
        else:
            print("There are no students in system")

    

    