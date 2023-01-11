#!/usr/bin/python3
"""
    Generate a list that contains a random number between 1 to 9
"""
import random

def generate():
    new_list = []
    for count in range(0, 5):
        n = random.randrange(1, 30)
        new_list.append(n)
    return new_list


print(generate())


