# Demonstration of Logic, Syntax, and Runtime Errors in Python

# ===== SYNTAX ERRORS =====
# Syntax errors occur when Python cannot parse the code
# Example: Missing colon after if statement
# if x > 5
#     print("x is greater than 5")

# Example: Incorrect indentation
# def greet():
# print("Hello")  # IndentationError

# ===== RUNTIME ERRORS =====
# Runtime errors occur during execution

# 1. ZeroDivisionError
print("--- ZeroDivisionError ---")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error caught: {e}")

# 2. NameError - variable not defined
print("\n--- NameError ---")
try:
    print(undefined_variable)
except NameError as e:
    print(f"Error caught: {e}")

# 3. TypeError - wrong data type
print("\n--- TypeError ---")
try:
    result = "5" + 5
except TypeError as e:
    print(f"Error caught: {e}")

# 4. IndexError - list index out of range
print("\n--- IndexError ---")
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"Error caught: {e}")

# ===== LOGIC ERRORS =====
# Logic errors occur when code runs but produces incorrect results

print("\n--- Logic Error Example ---")
# Purpose: Calculate average of numbers
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / 5  # Logic error: should be len(numbers), not hardcoded 5
print(f"Average: {average}")  # Works but might be wrong if list changes

# Correct version
correct_average = total / len(numbers)
print(f"Correct average: {correct_average}")

# Another logic error example: wrong comparison
print("\n--- Logic Error: Wrong Condition ---")
age = 15
if age > 18:  # Logic error: should check if age is >= 18 for adult
    print("You are an adult")
else:
    print("You are a minor")  # This executes, but might not match intent