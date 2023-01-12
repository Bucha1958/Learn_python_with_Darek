#!/usr/bin/python3
"""
    Bubble sort in reverse order
    Implement two looping system 
    Increment the first loop to move from left to right

"""
import random


new_list = []
for i in range(5):
    # Populate the list with random numbers by importing random
    new_list.append(random.randrange(0, 21))

var_1 = len(new_list) - 1

while var_1 > 1:
    var_2 = 0
    while var_2 < var_1:
        if new_list[var_2 + 1] > new_list[var_2]:
            temp = new_list[var_2 + 1]
            new_list[var_2 + 1] = new_list[var_2]
            new_list[var_2] = temp
        else:
            print()
        var_2 += 1
    var_1 -= 1

for k in new_list:
    print(k, end=", ")
print()
