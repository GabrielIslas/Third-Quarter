"""
Ejercicio 10
Escribir una clase en python llamada rectangulo que contenga una base y una altura, 
y que contenga un método que devuelva el área del rectángulo.
"""

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculateArea(self):
        return self.width * self.length
    
rectangle = Rectangle(5, 4)
print(rectangle.calculateArea())