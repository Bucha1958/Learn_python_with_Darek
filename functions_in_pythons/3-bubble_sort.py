#!/usr/bin/python3
"""
    Bubble Sort Algorithm steps
    The Bubble sort algorithm contains outer and inner loop
    An outer loop decreases in size each time
    The goal is to have the largest number at the end of the list when the outer loop completes one cycle
    Check if list[index] > list[index + 1]
    If so swap the index value
    When the inner loop completes, the largest number should be at the end of the list
    Decrement the outer loop by 1
"""
# from my own approach populate the list with looping and import random numbers
import random

num_list = []
for num in range(5):
    num_list.append(random.randrange(1, 10))

num = len(num_list) - 1

while num > 1:
    inner_var = 0
    # initiates the inner loop
    while inner_var < num:
        # check if the first index is greater than the second index
        if (num_list[inner_var] > num_list[inner_var + 1]):
        # during swaping create a temp variable that will store one of the list index
            temp = num_list[inner_var]
            num_list[inner_var] = num_list[inner_var + 1]
            num_list[inner_var + 1] = temp
        # Increment the inner variable to move from left to right
        inner_var += 1
    num -= 1

for k in num_list:
    print(k, end=", ")
print()



