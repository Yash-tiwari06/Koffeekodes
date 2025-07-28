new_dict = {}
def studentss(students_marks):
    if not students_marks:
        print("students are not in dictioney")



students = {
    "yash": [99, 88, 96, 92],
    "Arpit": [100, 100, 100, 100],
    "Neha": [70, 85, 88, 90],
    "Ravi": [60, 75, 80, 85]
}

new_dict = {}

for name, marks in students.items():
    for i in marks:
        if i < 90:
            new_dict.update() 
    print(new_dict)