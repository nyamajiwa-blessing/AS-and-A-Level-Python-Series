# Exceptions are errors that occur during runtime
num1 = 90
num2 = 0
pin = 1234 # integer
counter = 3
# try:
#     print(num1/num2)
# except Exception as e:
#     print("An error occured.")
#     print(e)
while counter != 0:
    try:
        attempt = int(input("Enter the PIN >>: "))
        if(attempt == pin):
            print("LOGIN SUCCESS")
            break
    except Exception as e:
        print("We encountered a problem.")
        print(e)
    finally: 
        counter = counter - 1
        print("You have ",counter," chances left.")

if counter == 0:
    print("ACCOUNT BLOCKED!")
