class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


a1 = Rectangle(10, 5)
print("area of rectangle is: ", a1.area())
print("perimeter of rectangle is: ", a1.perimeter())
