"""
Ejercicio 3
Escribir una clase en python para encontrar la validez de una cadena de paréntesis,'(', ')', '{', '}', '['  ']. 
Los paréntesis deben aparecer en el orden correcto, por ejemplo "()" y "()[]{}" son validos, 
pero "[)", "({[)]" y "{{{" son inválidos.
"""

class ParenthesesValidation:

    validOpeningSymbols = "([{"
    validClosingSymbols = ")]}"
    
    def __init__(self, string):
        self.string = string
        
    
    def validateParentheses(self):
        symbolStack = []
        for symbol in self.string:
            if symbol in self.validOpeningSymbols:
                symbolStack.append(symbol)
            elif symbol in self.validClosingSymbols:
                try:
                    extractedSymbol = symbolStack.pop()
                    if self.validClosingSymbols.index(symbol) != self.validOpeningSymbols.index(extractedSymbol):
                        print("Wrong closing symbol for opening symbol")
                        return False
                except IndexError:
                    print("Missing opening symbol for closing symbol")
                    return False
        if symbolStack:
            print("Missing closing symbols")
            return False
        return True     

string1 = "()[]{}"
string2 = "([{[()]}])"
string3 = "()[}]"
string4 = "({[)]"
string5 = "{{{"
string6 = ")()[]"
parentheses = ParenthesesValidation(string6)
print(parentheses.validateParentheses())