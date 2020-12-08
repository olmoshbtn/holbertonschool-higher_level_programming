#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#print all positive values
if number >= 0:
    #last digit > 5
    if (number % 10) > 5:
        print("Last digit of {} is {} and is grater than 5".format(number,\
                                                                (number % 10)))
    #last digit == 0
    if (number % 10) == 0:
        print("Last digit of {} is {} and is 0".format(number, (number % 10)))
    #last digit < 6 and != 0
    if (number % 10) < 6 and (number % 10) != 0:
        print("Last digit of {} is {} and is less than 6 and not 0"\
              .format(number, (number % 10)))
#print all negative values
else:
    print("Last digit of {} is {}{} and is less than 6 and not 0"\
          .format(number, (str(number)[:1]), (str(number)[-1:])))
