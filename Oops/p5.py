# School Management System (All-in-One File)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_profile(self):
        print(f"\n--- Profile ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = {}

    def add_marks(self, subject, score):
        self.marks[subject] = score
        print(f"{subject} marks added: {score}")

    def view_marks(self):
        print(f"\n{self.name}'s Marks:")
        for subject, score in self.marks.items():
            print(f"{subject}: {score}")


class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subjects = []

    def assign_subject(self, subject):
        self.subjects.append(subject)
        print(f"{subject} assigned to {self.name}")

    def view_subjects(self):
        print(f"\nSubjects taught by {self.name}:")
        for sub in self.subjects:
            print(f"- {sub}")


# Multilevel Inheritance
class Subject(Teacher):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age, teacher_id)

    def assign_to_student(self, student, subject):
        print(f"{self.name} assigned {subject} to {student.name}")


# Multiple Inheritance
class Admin(Student, Teacher):
    def __init__(self, name, age, admin_id):
        # Explicit call due to multiple inheritance
        Student.__init__(self, name, age, admin_id)
        Teacher.__init__(self, name, age, admin_id)
        self.admin_id = admin_id

    def full_access(self):
        print(f"Admin {self.name} has full access to student & teacher records.")


# --------- Testing -----------

# Create student and teacher
student1 = Student("Alice", 16, "S101")
teacher1 = Teacher("Mr. Smith", 35, "T500")

student1.view_profile()
teacher1.view_profile()

# Teacher assigns subject
teacher1.assign_subject("Math")
teacher1.assign_subject("Physics")
teacher1.view_subjects()

# Student receives marks
student1.add_marks("Math", 88)
student1.add_marks("Physics", 91)
student1.view_marks()

# Subject class (Multilevel)
sub = Subject("Mrs. Green", 40, "T201")
sub.assign_to_student(student1, "English")

# Admin (Multiple Inheritance)
admin1 = Admin("Principal Ray", 50, "A001")
admin1.full_access()
admin1.assign_subject("Biology")
admin1.view_subjects()
admin1.add_marks("Chemistry", 99)
admin1.view_marks()

