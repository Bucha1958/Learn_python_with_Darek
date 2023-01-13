#!/usr/bin/python3
players = [
        ['john', 'bill', 'tim', 'bob', 'jane', 'lisa', 'nicole', 'baron'],
        ['aron', 'walbert', 'henry', 'harry', 'margaret', 'jay'],
        ['steve', 'allan', 'mike', 'tom', 'lee', 'charles', 'sandy']
        ]


print("Row := {} has {} players".format(players.index(players[0]) + 1, len(players[0])))
for i in players[0]:
    print(i, end=", ")
print()
print("Row := {} has {} players".format(players.index(players[0]) + 2, len(players[1])))
for i in players[1]:
    print(i, end=", ")
print()




