#!/usr/bin/python3
"""
    Ceaser cipher is an encrypted method technique
"""
# Receive a message to encrypt
message = input("Please enter a text: ")
# Receive the key shift
key = int(input("Enter your shift key: "))
# Store the secret message
secret_message = ""
# Cycle through the message using looping
for char in message:
    # If character entered is not a letter don't shift it. Then check for letters
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        # Check for uppercase
        if char.isupper():
            # if bigger than Z substract 26
            if char_code > ord('Z'):
                char_code -= 26
            # if smaller than A then add 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        # Convert from code to letters and add to message
        secret_message += chr(char_code)
    else:
        secret_message += char
print("Encrypted: ", secret_message)
