# Same as list, but elements have no particular order
# 1. Defining a set using {}
subjects = {'Math','Geo','Eng','His'}
print(subjects)

# 2. Adding a single item to a set using add()
subjects.add('French')
print(subjects)
subjects.remove('Geo')
print(subjects)

# 3. Adding multiple items using update([])
subjects.update(['Geo','Bio'])
print(subjects)

# 4. Duplicating a set using copy()
a_copy = subjects.copy()
print("This is the new copy below...")
print(a_copy)