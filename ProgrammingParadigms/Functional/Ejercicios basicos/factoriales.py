factorial = lambda x: 1 if x == 0 else x * factorial(x-1)

factorialUpTo = lambda x: list(factorial(x) for x in range(0, x + 1))

evenFactorials = lambda x: list(factorial(x) for x in range(0, x + 1, 2))

print(evenFactorials(8))