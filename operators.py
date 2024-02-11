# Python follows PEMDAS rule. PEMDAS stands for Parentheses, Exponents, Multiplication and Division, and Addition
# and Subtraction.
num1 = 5
num2 = 14

name1 = "Dell"
name2 = "HP"
# arithmetic operators: +, -, /, %, *, ** and //
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num2 % num1)
print(num1 * num2)
print(num2 ** num1)
print(num2 // num1)

# logical/comparison for objects: is,  is not
print(name1 is not name2)
print(name1 is name1)

# boolean operators: or, and, not
company = "Acer"
if(company is not name1 and name1 is name1):
    print('This runs if either one of the above conditions is True') 
