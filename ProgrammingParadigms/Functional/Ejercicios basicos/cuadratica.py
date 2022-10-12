from math import sqrt

cuadratic = lambda a, b, c: ((-b + sqrt((b ** 2) - (4 * a * c)))/(2 * a), (-b - sqrt((b ** 2) - (4 * a * c)))/(2 * a))

coefficientA = float(input("Type coefficient a: "))
coefficientB = float(input("Type coefficient b: "))
coefficientC = float(input("Type coefficient c: "))

print(cuadratic(coefficientA, coefficientB, coefficientC))