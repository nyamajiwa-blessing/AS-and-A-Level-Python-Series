# Dunder methods (short for "double underscore methods") are special
# methods in Python that start and end with __
# Define how objectds behave e.g. how they print, compare and respond to operators

class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Person: {self.name}"

# p = Person("Bradley")
# print(p)        
class Basket:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

b = Basket(["apples","bananas","carrots"])
print(len(b))

# if __name__ == "__main__":