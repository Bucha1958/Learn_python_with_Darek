#!/usr/bin/python3
"""
    Populate a multidimensional list with random numbers 
    import a random module
"""

    

import random
new_list = [[random.randint(1, 10) for i in range(4)] for j in range(4)]


print(new_list)

"""
    Create a times table with multidimensional list
"""

for i in range(1, 10):
    for j in range(1, 11):
        result = i * j
        if j == 10:
            print()
        else:
            print(result, end=", ")
