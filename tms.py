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

    def assign_grade(self, fullname):
        self.subject = input("Enter the name of the subject: ")
        self.grade = int(input("Enter grade: "))
        for student in Student.students:
            if student["fullname"] == fullname:
                student[self.subject] = self.grade
                print("The student was graded!")

    def search_student(self, email):
        for student in Student.students:
            if student["email"] == email:
                for k, v in student.items():
                    print(k.capitalize() + ": ", v)
                break
        else:
            print("We don't have this student.")


print("Welcome to Student Management System!")
print("""You can choose one of these functions:
List students
Add student
Search student
Assign grade
Add and view announcement
Delete student""")

command = ""
while command != "Log out":
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

    elif command == "delete student":
        deleted_student = input("Student's fullname: ")
        for student in Student.students:
            if deleted_student == student["fullname"]:
                Student.students.remove(student)
                print("Student was deleted successfully!")
                break
        else:
            print("This student does not exist in the system.")

    elif command == "assign grade":
        graded_student = input("Student's fullname: ")
        for student in Student.students:
            if graded_student == student["fullname"]:
                std.assign_grade(graded_student)
                break
        else:
                print("This student does not exist in the system!")

    elif command == "search student":
        if Student.students:
            wanted_student = input("Enter the student's email: ")
            std.search_student(wanted_student)
        else:
            print("There are no students in system")

    

    