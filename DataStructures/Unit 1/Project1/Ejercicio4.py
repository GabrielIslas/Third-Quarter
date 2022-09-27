def pairSum(numberList, objective):
    differenceList = []
    pairList = []
    for index in range(len(numberList)):
        difference = objective - numberList[index]
        if difference in differenceList:
            indexPair = [difference, numberList[index]]
            pairList.append(indexPair)
        differenceList.append(numberList[index])
    return pairList

nl = [3,3,11,15]
o = 6

print(pairSum(nl, o))



