class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(self.name, "says woooff wooofff !!!")

    def sleep(self):
        print(self.name, "is sleeping....!!")
d = Dog("kalu", "pomerenian")
d.sleep()
d.bark()