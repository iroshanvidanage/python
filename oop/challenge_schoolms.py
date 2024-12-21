class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name}, age={self.age})'

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str) -> None:
        super().__init__(name, age)
        self.student_id = student_id
    
    def __str__(self) -> None:
        base_str = super().__str__()
        return f'{base_str.rstrip(")")}, student_id={self.student_id})'

class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str) -> None:
        super().__init__(name, age)
        self.subject = subject

    def __str__(self) -> None:
        base_str = super().__str__()
        return f'{base_str.rstrip(")")}, subject={self.subject})'

class Course:
    def __init__(self, name: str, teacher: str) -> None:
        self.name = name
        self.teacher = teacher
        self.students = []
    
    def search_student(self, name: str) -> Student:
        return next((student for student in self.students if student.name == name), None)

    def add_student(self, student: Student) -> None:
        # Implement the logic to add a student to the course
        chk_student = self.search_student(student.name)
        if chk_student:
            print(f'The student {student.name} is already enrolled to course {self.name}.')
            return
        else:
            self.students.append(student)
            print(f'The student {student.name} successfully enrolled to course {self.name}.')
            return
    
    def __str__(self) -> str:
        return f'Course(name={self.name}, teacher={self.teacher})'




# Example Usage
def test_example():
    teacher1 = Teacher("Mr. Smith", 40, "Mathematics")
    course1 = Course("Algebra 101", teacher1)

    student1 = Student("Alice", 16, "S123")
    student2 = Student("Bob", 17, "S124")

    course1.add_student(student1)
    course1.add_student(student1) # test scenario try to enroll twice
    course1.add_student(student2)


    # test __str__ implementation
    teacher2 = Teacher("Mr. Smith", 40, "Mathematics")
    
    student3 = Student("Alice", 16, "S123")
    student4 = Student("Bob", 17, "S124")
    
    print(teacher2)
    print(student3)
    print(student4)


if __name__ == '__main__':
    test_example()
