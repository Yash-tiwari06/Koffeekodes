class Shape:
    def area(self):
        raise NotImplementedError("Area method not implemented")
    
    def perimeter(self):
        raise NotImplementedError("Area method not implemented")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    def perimeter(self):
        return 2* 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(length + width)
c1 = Circle(5)
print(c1.area())
print(c1.perimeter())