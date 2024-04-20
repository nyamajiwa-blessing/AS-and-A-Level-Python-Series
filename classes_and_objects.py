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


