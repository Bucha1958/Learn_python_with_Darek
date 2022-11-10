#!/usr/bin/python3

num1, operator, num2 = input('Enter Calculation: ').split()

num1 = int(num1)
num2 = int(num2)

total = num1 + num2
diff = num1 - num2
product = num1 * num2
quotient = num1 / num2
modulus = num1 % num2

if (operator == '*'):
    print('{} * {} = {}'.format(num1, num2, product))
elif (operator == '+'):
    print('{} + {} = {}'.format(num1, num2, total))
elif (operator == '-'):
    print('{} - {} = {}'.format(num1, num2, diff))
elif (operator == '/'):
    print('{} / {} = {}'.format(num1, num2, quotient))
elif (operator == '%'):
    print('{} % {} = {}'.format(num1, num2, modulus))

