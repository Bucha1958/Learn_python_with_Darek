#!/usr/bin/python3
"""
    Ceaser cipher is a method for encryption
"""
# Ask the user to enter their text
message = input("Enter your text: ")
# Enter your keys
key = int(input("Please enter your shift keys: "))
# Secret Message
secret_message = ""
# Traverse through the text
for char in message:
    # Shift letters and don't shift non-letters
    # check for alphabets
    if char.isalpha():
        char_code = ord(char)
        # Add your shift keys
        char_code += key
        # Check for upper characters
        if char.isupper():
            # Check the addition of both exceeds the unicode of uppercase
            if char_code > ord('Z'):
                char_code -= 26
            # Check if the addition of the two is not close to the unicode of uppercase
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char
print("Encrypted Message: {}".format(secret_message))

key = -key
original_message = ""
# Traverse through the secret message
for char in secret_message:
    # shift letters and don't shift non-letters
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        # Check for uppercase letters
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        original_message += chr(char_code)
    else:
        original_message += char
print("Decrypted: {}".format(original_message))

