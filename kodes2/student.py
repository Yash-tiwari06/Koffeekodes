class Student:
    marks = 100
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_grade(self):
        if self.marks >= 90:
            print(f"Congratulations! {self.name} you have Grade A")
        elif self.marks >= 75:
            print(f"Congratulations! {self.name} you have Grade B")
        elif self.marks >= 50:
            print(f"{self.name} you need to prove yourself otherwise we'll kicked out you, have Grade C")
        else:
            print("Better luck next time broo !")
c1 = Student("Arpit", 92)
c1 =  Student("dubey ji", 35)
c1.get_grade()
