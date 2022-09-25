"""
Ejercicio 9
Escribir una clase en python con 2 métodos: get_string y print_string. 
get_string acepta una cadena ingresada por el usuario y 
print_string imprime la cadena en mayúsculas.
"""

class StringManipulation:
    
    def __init__(self):
        self.string = None
        
    def get_string(self):
        self.string = input("Type a string: ")
        
    def print_string(self):
        print(self.string.upper())
        
stringManipulation = StringManipulation()
stringManipulation.get_string()
stringManipulation.print_string()