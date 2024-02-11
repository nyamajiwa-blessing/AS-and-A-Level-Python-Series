# Functions in Python provide organized, reusable and modular code to perform a set of specific actions. Functions
# simplify the coding process, prevent redundant logic, and make the code easier to follow

# 1. Defining a function
def greeting():
    print("Hello World")

# 2. Calling a function
greeting()

# 3a. Function with argument(s)
def improved_greeting(message):
    print("Hello ",message)

improved_greeting('Python')
improved_greeting(263)
improved_greeting('Adam')

# 3b. Function with optional arguments
def even_better_greeting(msg = "Computer"):
    print("Hello ",msg)

even_better_greeting("Science")
even_better_greeting()

# 4. Function that returns a value
def square_number(num):
    return num * num

print(square_number(9))