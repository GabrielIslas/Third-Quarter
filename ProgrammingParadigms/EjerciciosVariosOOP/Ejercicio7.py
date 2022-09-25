"""
Ejercicio 7
Escribir una clase en python que calcule pow(x, n)
x = es la base
n = es el exponente
"""

class Power:
    
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent
    
    def pow(self):
        try:
            result = self.base ** self.exponent
        except ZeroDivisionError:
            return "Can't elevate 0 to a negative power"
        return result
        
power = Power(-1, 1/2)
print(power.pow())