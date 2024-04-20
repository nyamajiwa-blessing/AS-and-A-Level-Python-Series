#  Inheritance is a mechanism for creating a new class that specializes or modifies the
#  behavior of an existing class.The original class is called a base class or a superclass.The
#  new class is called a derived class or a subclass.When a class is created via inheritance, it
#  “inherits” the attributes defined by its base classes. However, a derived class may redefine
#  any of these attributes and add new attributes of its own.

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        return area
    
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

rect1 = Rectangle(50,12)
print("The area of rect1 is ",rect1.area())
print("The perimeter of rect1 is ",rect1.perimeter())

class Square(Rectangle):
    pass

square1 = Square(25,25)
print("The area of square1 is ",square1.area())
print("The perimeter of square1 is ",square1.perimeter())