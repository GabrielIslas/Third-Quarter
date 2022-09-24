# -*- coding: utf-8 -*-
"""
Ejercicio 1
Escribir una clase en python que convierta un número entero a número romano
"""

class IntToRoman:
    
    uniqueRomanSymbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    uniqueRomanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    def __init__(self, number):
        self.number = number.lstrip("0")
        
    def isPossible(self):
        romanNumberLimit = 3999
        if not self.number.isdigit():
            print("Number isn't an integer")
            return False
        elif int(self.number) > romanNumberLimit:
            print("Number is higher than the limit conversion")
            return False
        else:
            return True
        
    def toRoman(self):
        if not self.isPossible():
            return "Can't be converted"
        romanString = ""
        digitList = []
        maxNumberLength = 4
        numberLength = len(self.number)
        zeroAmount = maxNumberLength - numberLength
        for x in range(zeroAmount):
            digitList.append(0)
        for digit in self.number:
            digitList.append(int(digit))
        for x in range(4):
            digitList[3-x] *= 10**x
        
        print(digitList)
        
        for digitIndex in range(4):
            if digitList[digitIndex] == 0:
                continue
            individualRomanString = ""
            while digitList[digitIndex] > 0:
                for index in range(len(self.uniqueRomanValues)):
                    if self.uniqueRomanValues[index] <= digitList[digitIndex]:
                        individualRomanString += self.uniqueRomanSymbols[index]
                        digitList[digitIndex] -= self.uniqueRomanValues[index]
                        print(digitList[digitIndex])
                        break;
            romanString += individualRomanString
            print(digitList)
        return romanString
                        
testNumber = input("Type an integer: ")
convertIntToRoman = IntToRoman(testNumber)
print(convertIntToRoman.toRoman())
        
        
        
        
        
            
        
        
        