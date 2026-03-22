# Format printing in Python means embedding values into strings in a clean and readable manner.
# Eliminates messy string concatenation.
name = "Alice"
age = 25

print("Name: " + name + ", Age: ",age)
print("Name: " + name + ", Age: "+ str(age))
print("-----------------------------------")
# Using f-printing
print(f"Name: {name}, Age: {age}")

a = 45
b = 45
print(f"The sum of {a} and {b} is {a + b}")

price = 49.96874
print(f"The price is {price:.2f}")

# Padding and alignment
name = "Bob"
print(f"{name:10}") #left-aligned
print(f"{name:>10}") #right-aligned
print(f"{name:^10}") #centred

# Leading zeros in integers
james_bond = 7
print(f"James Bond is the OG {james_bond:03}")

# Printing large numbers
salary = 1500000
print(f"The annual salary is {salary:,}")

# Using the format method
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name,age))