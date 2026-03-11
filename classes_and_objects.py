# Class: A collection of functions and attributes, attached to a specific name, which represents an abstract concept. 
# Attribute: A named piece of data (i.e. variable associated with a class.
# Object: A single concrete instance generated from a class

class Customer:
    def __init__(self, name, balance, status):
        self.name = name
        self.balance = balance
        self.status = status
    
    def display_info(self):
        print("Name of customer: ", self.name)
        print("Current account balance is: ", self.balance)
        print("The customer activation status is: ", self.status)

c1 = Customer("Tom Cruise",450,True)
c2 = Customer("Tony Stark",800,False)
c3 = Customer("Jason Statham",200,True)

c1.display_info()
print()
c2.display_info()
print()
c3.display_info()


# Composite data type: Class
class Student:
    def __init__(self, name, age, gpa):
        self.name = name    # string
        self.age = age      # integer
        self.gpa = gpa      # float

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("GPA:", self.gpa)


# Creating an object
s1 = Student("Alice", 20, 3.6)
s1.display_info()

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.speed += 10

car1 = Car("Red", 50)   # Object
car2 = Car("Blue", 0)   # Object

car1.accelerate()
print(car1.speed)  # 60

