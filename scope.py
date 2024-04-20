price = 9.99
print(price)

def x():
    global items
    print(price)
x()
items = 45
print(items)

def outer():
    name = "User"
    print(name)
    def inner():
        nonlocal name # makes variable belong to the outer function
        name = "Admin"
    inner()
    return name

print(outer())
