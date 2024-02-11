# An array is a data structure that stores values of same data type. In Python, this is the main difference between
# arrays and lists.

# 1. Importing the array module
from array import *

# 2. Creating an array: array(typecode) e.g. 'i','f' and 'c' 
numbers_array = array('i',[1,2,3,4,5])
print(numbers_array)

# 3. Adding new item using insert(i, item)
numbers_array.insert(2,99)
print(numbers_array)

# 4. Remove specific item using remove(item)
numbers_array.remove(4)
print(numbers_array)

# 5. Remove using index pop(index)
numbers_array.pop(0)
print(numbers_array)