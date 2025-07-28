class Employee:
    total_employee = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employee += 1

    
    def display_details(self):
        print(f"Name:{self.name}")
        print(f"salary:{self.salary}")
    
    @classmethod
    def display_total_employees(cls):
        print(f"Total employees:{cls.total_employee}")

emp1 = Employee("Arpit", 45000)
emp1.display_details()
emp1.display_total_employees()