# -*- coding: utf-8 -*-
"""
wow 2
"""



def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
fib = int(input("Type which Fibonacci number you want: "))
print(Fibonacci(fib))
  
