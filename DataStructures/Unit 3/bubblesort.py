def bubble_sort1(list):
    length = len(list)
    while True:
        n = 0
        for i in range(1, length):
            if list[i] < list[i-1]:
                temp = list[i]
                list[i] = list[i-1]
                list[i-1] = temp
                n = i
                print(list)
        length = n
        print("Pasada")
        if n == 0:
            break

def bubble_sort2(list):
    exchange = True
    passedNumber = len(list) - 1
    passedTimes = 0
    while passedNumber > 0 and exchange:
        passedTimes += 1
        exchange = False
        for i in range(passedNumber):
            if list[i] > list[i+1]:
                exchange = True
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        passedNumber = passedNumber - 1
        print(list)
        print(f"Pasada {passedTimes}")

list1 = [5, 4, 3, 2, 1]
list2 = [3, 7, 1, 7, 8, 2, 5]
list3 = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
list4 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
list5 = [1, 2, 3, 4, 5]
bubble_sort2(list3)

# Respuesta B
    

        
        
