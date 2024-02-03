# Identation is everything
# Python uses indentation to define control and loop constructs.
# Dynamically-typed
# This contributes to Python's readability, however, itrequires the programmer to pay close attention to the use of whitespace
# Python keywords

import keyword
reserved_keywords = keyword.kwlist
count = 0
# print(reserved_keywords)
for word in reserved_keywords:
    print(word)
    count = count + 1

print("Python has a total of ",count, " keywords.")

