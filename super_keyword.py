# super() function is used to call methods from a parent(superclass) inside a child(subclass)
# Useful in inheritance to avoid directly referencing the parent class name
import math

class Shape:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        print(f"This is a {self.name}")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle") # Calling the superclass constructor
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def describe(self):
        super().describe() # Extending the parent describe() method
        print(f"Width: {self.width}, Height: {self.height}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def describe(self):
        super().describe()
        print(f"Radius: {self.radius}")
        
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def describe(self):
        super().describe()
        print(f"Base: {self.base}, Height: {self.height}")

rect = Rectangle(7, 10)
circ = Circle(3)
tria = Triangle(12, 9)

my_shapes = [rect, circ, tria]

for shape in my_shapes:
    shape.describe()
    print(f"Area: {shape.area()}")
    print("-" * 20)