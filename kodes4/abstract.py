from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod 
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("woooff !")

class Cat(Animal):
    def make_sound(self):
        print("Meoww !")

class Bird(Animal):
    def make_sound(self):
        print("piuuhh piuhhh !")

c = Cat()
c.make_sound()

d = Dog()
d.make_sound()

b = Bird()
b.make_sound()