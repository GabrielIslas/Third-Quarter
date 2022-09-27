"""
Exercise 1
Given 2 lists, find the elements that are in one list an not in another list
"""

def uniqueElements(list1, list2):
    listResult = []
    
    for x in list1:
        if x not in list2:
            listResult.append(x)

    for x in list2:
        if x not in list1:
            listResult.append(x)

    print(listResult)


list1 = [1,2,3,5,6]
list2 = [6,3,2,3]
uniqueElements(list1, list2)

