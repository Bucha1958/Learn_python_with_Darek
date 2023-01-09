#!/usr/bin/python3

# Ask the user to enter a number, if otherwise print error message


while True:
    try:
        enter_number = int(input("Please enter a number: "))
        if type(enter_number) == int:
            break
    except (ValueError, TypeError, NameError):
        print("Please put integer")
    except:
        print("It is wrong")

