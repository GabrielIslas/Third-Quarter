"""
Ejercicio 2
Escribir una clase en python que convierta un número romano en un número entero
"""

class RomanToInt:
    
    uniqueRomanSymbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    uniqueRomanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    def __init__(self, number):
        self.number = number.upper()
        
    def areSymbolsValid(self):
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
        return tokens

    def isOrderValid(self, tokens):
        previousSymbolValue = 2000
        for token in tokens:
            currentTokenValue = self.uniqueRomanValues[self.uniqueRomanSymbols.index(token)]
            if previousSymbolValue + currentTokenValue in self.uniqueRomanValues:
                return False
            if currentTokenValue <= previousSymbolValue:
                previousSymbolValue = currentTokenValue
            else:
                return False
        return True
    
    def areSymbolsRepeating(self, tokens):
        symbolRepeat = 0
        previousSymbol = None
        for token in tokens:
            tokenCanRepeat = token ==  "M" or token == "C" or token == "X" or token == "I"
            if previousSymbol != token:
                previousSymbol = token
                if tokenCanRepeat:
                    symbolRepeat = 1
                else:
                    symbolRepeat = 3
            elif previousSymbol == token:
                symbolRepeat += 1
            if symbolRepeat == 4:
                return True
        return False

    def toInt(self):
        if not self.areSymbolsValid():
            return "Can't be converted, symbols aren't valid"
        
        tokens = self.romanTokens()
        
        if not self.isOrderValid(tokens):
            return "Can't be converted, order of symbols isn't valid"
        
        if self.areSymbolsRepeating(tokens):
            return "Can't be converted, invalid repetition of symbols"
        
        intValue = 0
        
        for token in tokens:
            intValue += self.uniqueRomanValues[self.uniqueRomanSymbols.index(token)]
        
        return intValue
        
testRoman = input("Type a roman number: ")
romanNumber = RomanToInt(testRoman)
print(romanNumber.toInt())