factorial = lambda x: 1 if x == 0 else x * factorial(x-1)

number = int(input("Type a number: "))
print(factorial(number))