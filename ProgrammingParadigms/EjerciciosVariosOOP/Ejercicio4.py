"""
Ejercicio 4
Escribir una clase en python que obtenga todos los posibles
subconjuntos únicos de un conjunto de números enteros distintos.
"""

import itertools

class Subsets:
    
    def __init__(self, Set):
        self.Set = Set
        
    def subsets(self):
        subsetList = []
        for size in range(len(self.Set) + 1):
            sizeSubset = list(itertools.combinations(self.Set, size))
            subsetList += sizeSubset
        for index in range(len(subsetList)):
            subsetList[index] = set(subsetList[index])
        return subsetList
    
Set = {4, 5, 6}
subsets = Subsets(Set)
print(subsets.subsets())

