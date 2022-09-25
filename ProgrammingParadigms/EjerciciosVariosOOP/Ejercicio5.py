"""
Ejercicio 5
Escribir una clase en python que encuentre un par de elementos (índice de los números) 
de una matriz dada cuya suma es igual a un número de destino especifico.
"""

class PairSum:
    
    def __init__(self, numberList, objective):
        self.numberList = numberList
        self.objective = objective
        
    def findPair(self):
        differenceList = []
        for index in range(len(self.numberList)):
            difference = self.objective - self.numberList[index] 
            if difference in differenceList:
                indexPair = [differenceList.index(difference), index]
                return indexPair
            differenceList.append(self.numberList[index])
        return "Not found"
    
nl = [3,3,11,15]
o = 6
pairSum = PairSum(nl, o)
print(pairSum.findPair())
            