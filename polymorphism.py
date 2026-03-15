# Polymorphism is the ability of different objects to respond to the same method or function call in different ways.
# Importance:
#   1. Flexible code
#   2. Code reuse
#   3. Code extensibility
#   4. Clean OOP design

# Polymorphism with built-in functions
print(25)
print("hello")
print(8.25)
print(len("hello")) #string
print(len((10,20,30))) #tuple
print(len([1,2,3,4,5])) #list

print("-----------------------------------------")
# Polymorphism with user-defined functions
def print_length(item):
    print(len(item))

print_length("Python Programming")
print_length([1,2,3,4,5])

# Polymorphism with operators
print("-----------------------------------------")
print(5 + 3)
print("Hello " + "World")
print([1,2,3] + [4,6])

# Polymorphism with Class methods (method overriding)
print("-----------------------------------------")
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()