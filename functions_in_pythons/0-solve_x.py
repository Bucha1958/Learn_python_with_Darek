#!/usr/bin/python3
"""
    Solve for x in algebraic equation x + 4 = 12
"""
# Split the string and assign them to individual variables by using unpacking
# x will always be the first value received and you only will deal with addition

def solve_x(x =""):
    x, add, num1, equal, num2 = x.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)
print(solve_x("x + 10 = 12"))

# Learn how to return multiple value in functions

def multi_values(nome, denom):
    return (nome * denom), (nome / denom)
multi, divide = multi_values(5, 4)
print(multi)
print(divide)

"""
    How to return a list of primes. prime number can only be divide by 1 or itself
"""

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def get_primes(max_num):
    list_of_primes = []
    for count in range(2, max_num):
        if (is_prime(count)):
            list_of_primes.append(count)
    return list_of_primes

max_value = int(input("Maximum number: "))
list_of_primes = get_primes(max_value)
for prime in list_of_primes:
    print(prime)


"""
    How to deal with unknown number been passed to the function
"""

def sum_all(*args):
    sum = 0
    for i in args:
        sum += i   
    return sum

print("Sum: ", sum_all(1, 2, 3, 4, 5))

