#!/usr/bin/python3

money = input('Enter amount to be invested: ')
interest_rate = input('Expected interest: ')

#convert to float from string
money = float(money)
#convert interest_rate from string to float and convert to percentage
interest_rate = float(interest_rate) * 1 / 100

for i in range(10):
    money = money + (money * interest_rate)
print('Amount after 10 years: {:.0f}'.format(money))

