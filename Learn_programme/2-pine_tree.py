#!/usr/bin/python3

# Enter the length of the tree
length = input('Enter the length of the tree: ')
# convert length to integer
length = int(length)
# Enter the no of spaces 
space = length - 1
# First harsh start with one will increment by one
harsh = 1
# save the first harsh for future use
save_stump = length - 1
# make sure the right number of rows are painted
while length != 0:
    for i in range(space):
        print(' ', end="")
    for i in range(harsh):
        print('#', end="")
    print()
    space -= 1
    harsh += 2
    length -= 1
for i in range(save_stump):
    print(' ', end="")
print('#')
