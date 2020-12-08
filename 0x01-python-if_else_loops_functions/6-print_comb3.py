#!/usr/bin/python3
for number in range(1, 10):
    print('{:02d}'.format(number), ',', sep='', end=' ')
for number in range(12, 80):
    number = str(number)
    if number[0] != number[1] and number[0] < number[1]:
        print('{:02d}'.format(int(number)), ',', sep='', end=' ')
print('89')
