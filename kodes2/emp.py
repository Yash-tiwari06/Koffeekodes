class Employeee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def apply_raise(self):
        self.salary += self.salary * 0.10
        print(f"{self.name}'s new salary add after 10% raise{self.salary}")
em = Employeee("yash", 60000)
print(em.name, em.salary)
em.apply_raise()