"""
Ejercicio 8
Escribir una clase en python que revierta una cadena de palabras
"""

class ReverseWords:
    
    def __init__(self, string):
        self.string = string
        
    def reverse(self):
        wordList = self.string.split(" ")
        wordList.reverse()
        reverseString = ""
        for word in wordList:
            reverseString += word
            reverseString += " "
        return reverseString
    
reverse = ReverseWords("asd jhkasd dsahj jsak")
print(reverse.reverse())