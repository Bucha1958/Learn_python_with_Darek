#!/usr/bin/python3
"""
    Ask the user to enter a string and the program converts those strings to acronyms
"""
# Ask for a string
enter_string = input("Enter a string: ")
# convert the string to uppercase
enter_string = enter_string.upper()
# Convert the string into a list
enter_string = enter_string.split()
# Cycle through the list
for word in enter_string:
    print(word[0], end="")
print()
