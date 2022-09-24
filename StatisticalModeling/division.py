try:
    number1 = float(input("Type number 1: "))
except ValueError:
    print("Error: not a number")
    exit()
try:
    number2 = float(input("Type number 2: "))
except ValueError:
    print("Error: not a number")
    exit()

if number2 == 0:
    print("Error: Can't divide by 0")
    exit()

print(number1/number2)