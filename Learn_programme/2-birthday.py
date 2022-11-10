#!/usr/bin/python3

age = eval(input('Enter your Age: '))

if (age < 5):
    print('Too young for school')
elif (age > 5) and (age <= 17):
    grade = age - 5
    print('Go to grade {}'.format(grade))
else:
    print('Go to College')

