# -*- coding: utf-8 -*-
"""
Ejercicio 2
Escribir una clase en python que convierta un número romano en un número entero
"""

class RomanToInt:
    
    uniqueRomanSymbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    uniqueRomanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    def __init__(self, number):
        self.number = number
        
    def validSymbols(self):
        for char in self.number:
            if char not in self.uniqueRomanSymbols:
                return False
        return True
        
    def romanTokens(self):
        numberAux = self.number
        tokens = []
        while len(numberAux) > 0:
            for symbol in self.uniqueRomanSymbols:
                if numberAux.startswith(symbol):
                    tokens.append(symbol)
                    numberAux = numberAux.removeprefix(symbol)
                    break
        print(self.isPossible(tokens))
        return tokens

    def isPossible(self, tokens):
        symbolValue = 2000
        for token in tokens:
            currentTokenValue = self.uniqueRomanValues[self.uniqueRomanSymbols.index(token)]
            if currentTokenValue <= symbolValue:
                symbolValue = currentTokenValue
            else:
                return False
        return True
        
    def toInt(self):
        
        return 1
        
roman = "MMCDXXXII"
romanNumber = RomanToInt(roman)
print(romanNumber.romanTokens())