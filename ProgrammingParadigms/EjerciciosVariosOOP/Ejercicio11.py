"""
Ejercicio 11
Escribir una clase en python llamada circulo que contenga un radio,
con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def calculatePerimeter(self):
        return math.pi * self.radius * 2
    
    def calculateArea(self):
        return math.pi * self.radius ** 2
    
circle = Circle(5)
print(circle.calculateArea())
print(circle.calculatePerimeter())