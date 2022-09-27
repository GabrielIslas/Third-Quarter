"""
Ejercicio 2
Given 2 lists of numbers, verify that they are equal, that they contain the same values
Return true if they are the same and false if they are different
"""

def areValuesEqual(list1, list2):
    if len(list1) != len(list2):
        return False
    for x in list1:
        if x in list2:
            list2.pop(list2.index(x))
        else:
            return False
    return True




list1 = [1,1,2,4,5,6]
list2 = [6,5,4,1,2,3]
print(areValuesEqual(list1, list2))



