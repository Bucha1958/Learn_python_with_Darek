#!/usr/bin/python3
# Enter a secret message to hide in uppercase
# Secret Message
# Original Message

enter_message = input(" ")
new = ""
new_one = ""
for i in enter_message:
    new += str(ord(i))
print("Secret Message: {}".format(new), end="")
print()
for name in enter_message:
    new_one += name
print("Original Message: {}".format(new_one), end="")
print()
