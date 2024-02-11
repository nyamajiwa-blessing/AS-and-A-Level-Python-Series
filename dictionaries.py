# A dictionary is an example of a key value store also known as Mapping in Python. It allows you to store and retrieve
# elements by referencing a key.

# 1. Creating a dictionary
countries = {'zw':'Zimbabwe','za':'South Africa','bot':'Botswana','us':'United States'}
print(countries)

# 2. Using get() to retrieve a value from a dictionary
print(countries.get('zw'))

# 3. Update a value in dictionary using update()
# countries.update('zw':'ZIMBABWE')
countries.update({'zw':'ZIMBABWE'})
print(countries)

# 4. See available keys using keys()
print(countries.keys())
