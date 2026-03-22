# Basic value matching
day = "Sunday"

match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("End of the work week")
    case "Saturday" | "Sunday":
        print("It's the weekend")
    case _:
        print("No matching value found.")
    
# Matching multiple values
status = 404

match status:
    case 200:
        print("Success")
    case 400 | 401 | 403:
        print("Client error")
    case 404:
        print("Not found")
    case _:
        print("Unknown status.")
        
# Matching data structures
data = [1,2,4,5]

match data:
    case [x,y]:
        print(f"Two numbers: {x} and {y}")
    case [x,y,z]:
        print("Three numbers")
    case _:
        print("Other pattern.")

# Matching with conditions (guards)
number = -15

match number:
    case n if n < 0:
        print("Negative number.")
    case n if n == 0:
        print("Zero.")
    case n if n > 0:
        print("Positive number.")