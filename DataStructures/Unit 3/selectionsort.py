def selection_sort(list):
    sorted = 0
    while sorted != len(list): # continue until every number has been put in the right place
        smallest = list[sorted] 
        smallestIndex = sorted
        for i in range(sorted, len(list)): # find smallest number
            if list[i] < smallest:
                smallest = list[i]
                smallestIndex = i
        print(list)
        print(f"Se coloca {smallest} en la posicion {sorted + 1}: Se cambia el {smallest} con el {list[sorted]}")
        list[smallestIndex] = list[sorted] # place smallest numbers in order as they are found
        list[sorted] = smallest
        sorted += 1
    return list

list1 = [40, 21, 4, 9, 10, 35]
print(selection_sort(list1))

