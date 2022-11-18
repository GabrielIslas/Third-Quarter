def selection_sort(list):
    sorted = 0
    while sorted != len(list):
        smallest = list[sorted]
        smallestIndex = sorted
        for i in range(sorted, len(list)):
            if list[i] < smallest:
                smallest = list[i]
                smallestIndex = i
        list[smallestIndex] = list[sorted]
        list[sorted] = smallest
        sorted += 1
    return list

list1 = [5, 4, 3, 2, 1]
list2 = [6, 8, 4, 10, 70, 52, 31]
print(selection_sort(list2))
