"""
Exercise 1
Given 2 lists, find the elements that are in one list an not in another list
"""

def uniqueElements(list1, list2):
    listResult = [] # list where results are saved
    # if element in list 1 is not in list 2, then it is unique
    for number in list1:
        if number not in list2:
            listResult.append(x)
    # if element in list 2 is not in list 1, then it is unique
    for number in list2:
        if number not in list1:
            listResult.append(x)
    # print list of unique elements
    print(listResult)

list1 = [1,2,3,5,6]
list2 = [6,3,2,3]
uniqueElements(list1, list2)

