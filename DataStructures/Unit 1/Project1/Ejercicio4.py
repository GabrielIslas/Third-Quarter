def pairSum(numberList, objective):
    # a list of differences and the list of pairs to be printed
    differenceList = []
    pairList = []
    # check each numbers difference with its objective
    # if that difference is in the difference list, that means that the current number
    # and one previously found are a pair that works
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



