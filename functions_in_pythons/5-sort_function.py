#!/usr/bin/python3
"""
    Write a function that sorts a list in ascending order
"""

def sort_1(old_list):
    new_list = []
    num_1 = len(old_list) - 1
    while num_1 > 1:
        num_2 = 0
        while num_2 < num_1:
            if old_list[num_2] > old_list[num_2 + 1]:
                temp = old_list[num_2]
                old_list[num_2] = old_list[num_2 + 1]
                old_list[num_2 + 1] = temp
            num_2 += 1
        num_1 -= 1
    for i in old_list:
        new_list.append(i)
    print(new_list)

def main():

    new_list = [2, 3, 1, 8, 5]

    sort_1(new_list)

main()
