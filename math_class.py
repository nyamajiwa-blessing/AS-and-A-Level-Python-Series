import math as m

num1 = 81
name = "Python"
print(m.sqrt(num1))
try:
    print(m.isnan(name))
except Exception as e:
    print(e)