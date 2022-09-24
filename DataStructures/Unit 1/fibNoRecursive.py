# -*- coding: utf-8 -*-
"""
wow
"""

x = 0
y = 1
z = 0

amount = int(input("Type how many Fibonacci numbers you want: "))

while amount > 0:
    print(x)
    z = x + y
    x = y
    y = z
    amount = amount - 1
    