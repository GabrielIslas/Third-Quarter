
def insertion_sort(list):
    for i in range(1, len(list)): # start with 1, first element assumed to be ordered
        element_check = list[i]
        j = i
        # print sublists
        print(f"Sublista {i}: [ ", end="")
        for k in range(i):
            print(f"{list[k]} ", end = "")
        print("]")
        # end print sublists
        while j > 0 and element_check < list[j-1]: # check backwards where to insert
            list[j] = list[j-1]
            j -= 1
        list[j] = element_check    
    return list

list1 = [40, 21, 4, 9, 10, 35]
print(f"Lista final: {insertion_sort(list1)}")



                



