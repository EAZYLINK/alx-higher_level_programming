#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -1 * number
    num = -1 * (number % 10)
    number = -1 * number
else:
    num = number % 10
if num > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, num))
elif num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
elif num <= 5 and num != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, num))
