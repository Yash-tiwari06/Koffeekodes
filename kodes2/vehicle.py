class Vehicle:
    def __init__(self, speed, color):
        self.speed = speed 
        self.color = color
    def info(self):
        print(self.speed)
        print(self.color)

class Car(Vehicle):
    def honk(self):
        print("car says: Beep Beep !")
class Bike(Vehicle):
    def honk(self):
        print("Bike says: thoo thoo")
car1 = Car(500, "black")
bike1 = Bike(600, "white")
print(bike1.info())
print(car1.info())
car1.honk()
bike1.honk()