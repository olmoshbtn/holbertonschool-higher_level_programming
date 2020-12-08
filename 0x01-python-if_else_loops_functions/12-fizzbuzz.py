#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            val = 'FizzBuzz'
        elif num % 5 == 0:
            val = 'Buzz'
        elif num % 3 == 0:
            val = 'Fizz'
        else:
            val = num
        print('{} '.format(val), end='')
