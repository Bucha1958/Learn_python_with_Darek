#!/usr/bin/python3

"""
    Bubble sort in descending order
"""

def descending_order(list_1):
    new_list = []
    i = len(list_1) - 1
    while i > 0:
        j = 0
        while j < i:
            if list_1[j + 1] > list_1[j]:
                temp = list_1[j + 1]
                list_1[j + 1] = list_1[j]
                list_1[j] = temp
            j += 1
        i -= 1
    for count in list_1:
        new_list.append(count)
    print(new_list)


def main():

    new_list = [8, 3, 1, 4, 9, 7]

    descending_order(new_list)

main()
