def bubble_sort2(list):
    exchange = True
    passedNumber = len(list) - 1
    passedTimes = 0
    while passedNumber > 0 and exchange:
        # passednumber used as max amount of passes to order list
        # if no exchanges are made in a pass, end early
        passedTimes += 1
        exchange = False
        print(f"Pasada {passedTimes}")
        for i in range(passedNumber):
            if list[i] > list[i+1]:
                print(f"Se cambia el {list[i]} por el {list[i+1]}")
                exchange = True
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        passedNumber = passedNumber - 1
        print(list)

list1 = [40, 21, 4, 9, 10, 35]
bubble_sort2(list1)
    

        
        
