# Anonymous functions in the form of an expression can be created using the lambda
# statement: lambda args : expr
def sum(num1, num2):
    return num1 + num2

print(sum(10,90))

# defining a lambda
product = lambda a,b : a * b
result = product(9,9)
print(result)
