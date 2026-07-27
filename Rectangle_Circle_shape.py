import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Test
rect = Rectangle(5, 3)
print(f"Rectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")

circle = Circle(4)
print(f"Circle Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")

