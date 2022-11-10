#!/usr/bin/python3

num1, num2 = input('Enter two numbers: ').split()

num1 = int(num1)
num2 = int(num2)

total = num1 + num2
diff = num1 - num2
product = num1 * num2
quotient = num1 / num2
modulus = num1 % num2

print("{} + {} = {}".format(num1, num2, total))
print("{} - {} = {}".format(num1, num2, diff))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, modulus))
