# lists are sequences of arbitrary objects
# a mutable data structure

# creating a list using [] or list()
fruits = ["apples","bananas","carrots","damplings"]
people = ["Anna","Beaulah","Chelsea","Darren"]
combined = list()

# accessing elements of a list
print(fruits[3])
print(people[2])

# adding new items to the end of a list using append()
fruits.append("oranges")
print(fruits)

# adding new items to any position of a list using insert()
fruits.insert(0,"pineapples")
print(fruits)

# slicing a list using :
print(people[0:2])

# joinig two lists using + 
combined = fruits + people
print(combined)
