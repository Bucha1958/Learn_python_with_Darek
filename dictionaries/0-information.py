#!/usr/bin/python3
"""
    This program will ask the customer to put there name and print it out on the screen
"""
# Create an empty dictionaries
dict_t = {}


def main():
    while True:
        ask_to_enter = input("Enter Customer (Yes/No): ")
        ask_to_enter = ask_to_enter.lower()
        if ask_to_enter == "yes" or ask_to_enter == "y":
            name, last = input("Enter name : ").split()
            dict_t[name] = last
        elif ask_to_enter == "no" or ask_to_enter == "n":
            for k, v in dict_t.items():
                print(k, v)
            break

main()
