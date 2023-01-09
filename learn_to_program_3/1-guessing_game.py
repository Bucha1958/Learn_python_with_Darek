#!/usr/bin/python3
# Guess a number between 1 to 10
import random
secret_number = 7

while True:
    guess_number = int(input("Please enter a number: "))
    if guess_number == secret_number:
        print("Congratulations you won!")
        break
    else:
        print("Please try again")


