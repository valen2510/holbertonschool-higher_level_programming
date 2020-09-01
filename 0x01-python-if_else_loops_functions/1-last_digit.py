#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
lst = n % 10 if n > 0 else -n % 10
if n < 0:
    lst *= -1
if lst == 0:
    print("Last digit of {} is {} and is 0".format(n, lst))
elif lst < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, lst))
else:
    print("Last digit of {} is {} and is greater than 5".format(n, lst))
