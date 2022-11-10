#!/usr/bin/python3
# The number of rows 
number_of_rows = input('Enter the number of rows: ')
# convert the number of rows into integer
number_of_rows = int(number_of_rows)
# Starting space
space = number_of_rows - 1
# number of harshes
harsh = 1
# Get the accurate number of rows
while number_of_rows != 0:
# print the spaces
    for i in range(space):
        print(' ', end="")
    for i in range(harsh):
        print('#', end="")
    print()
    space -= 1
    harsh += 2
    number_of_rows -= 1
for i in range(space):
    print(' ', end="")
print("#")
