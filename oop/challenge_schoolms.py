class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        # Implement the logic to add a student to the course

# Example Usage
teacher = Teacher("Mr. Smith", 40, "Mathematics")
course = Course("Algebra 101", teacher)

student1 = Student("Alice", 16, "S123")
student2 = Student("Bob", 17, "S124")

course.add_student(student1)
course.add_student(student2)
