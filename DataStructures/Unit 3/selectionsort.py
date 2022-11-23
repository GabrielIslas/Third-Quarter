def selection_sort(list):
    sorted = 0
    while sorted != len(list):
        smallest = list[sorted]
        smallestIndex = sorted
        found = False
        for i in range(sorted, len(list)):
            if list[i] < smallest:
                smallest = list[i]
                smallestIndex = i
        print(f"Selected smallest number is {smallest} in index {smallestIndex} and it should be in {sorted}.")
        print(list)
        list[smallestIndex] = list[sorted]
        list[sorted] = smallest
        sorted += 1
    return list

list1 = [5, 4, 3, 2, 1]
list2 = [6, 8, 4, 10, 70, 52, 31]
list3 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
selection_sort(list3)

