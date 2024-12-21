class Employee:
    def __init__(self, name: str, employee_id: str) -> None:
        self.name = name
        self.employee_id = employee_id
        self.department = None
        self.projects = []

    def assign_department(self, department) -> None:
        # Implement the logic to assign an employee to a department

    def assign_project(self, project) -> None:
        # Implement the logic to assign an employee to a project

    def __str__(self) -> str:
        return f'Employee(name={self.name}, employee_id={self.employee_id})'

class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee) -> None:
        # Implement the logic to add an employee to the department

    def __str__(self) -> str:
        return f'Department(name={self.name}, employees={len(self.employees)})'

class Project:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee) -> None:
        # Implement the logic to add an employee to the project

    def __str__(self) -> str:
        return f'Project(name={self.name}, employees={len(self.employees)})'

# Example Usage
def test_example() -> None:
    employee1 = Employee("Alice", "E001")
    employee2 = Employee("Bob", "E002")

    department = Department("Engineering")
    project = Project("Project X")

    department.add_employee(employee1)
    project.add_employee(employee1)

    department.add_employee(employee2)
    project.add_employee(employee2)

    print(department)
    print(project)
    print(employee1)
    print(employee2)

if __name__ == '__main__':
    test_example()
