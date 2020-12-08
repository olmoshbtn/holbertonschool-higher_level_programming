#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# last digit capture
last_digit = abs(number) % 10
# change value for negative last digit
if number < 0:
    last_digit *= -1
# last digit > 5
if last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_digit))
# last digit == 0
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
# last digit < 6 and != 0
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit))
