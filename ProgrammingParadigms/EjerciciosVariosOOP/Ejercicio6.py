"""
Ejercicio 6
Escribir una clase en python que encuentre los 3 elementos que sumen 0 a partir de números reales
"""

import itertools

class ZeroSum:
    
    def __init__(self, numberList):
        self.numberList = numberList
        
    def combinationsOf3(self):
        return list(itertools.combinations(self.numberList, 3))
    
    def findZeroSum(self):
        combinationsList = self.combinationsOf3()
        zeroSumList = []
        for combination in combinationsList:
            if sum(combination) == 0:
                zeroSumList.append(combination)
        return zeroSumList
    
nl = [-25, -10, -7, -3, 2, 4, 8, 10]
zerosum = ZeroSum(nl)
print(zerosum.findZeroSum())