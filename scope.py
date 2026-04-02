# Scope - refers to the visibility / accessibility of variables
sum = 45

def add_two(x,y):
    global sum
    print(sum)
    sum = x + y
    print (sum)

add_two(1,2)
print("=================================================================")
# Using nonlocal
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

c = counter()
print(c())
print(c())