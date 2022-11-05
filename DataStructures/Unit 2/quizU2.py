vector = []
size = int(input("Type the size of the vector: "))

menu = True
while menu:
    print("1. Add element")
    print("2. Delete element")
    print("3. Print vector content")
    print("4. Count amount of numbers")
    print("5. Max and mean")
    print("0. End program")
    option = input("Type the option: ")
    if option == "0":
        menu = False
    elif option == "1":
        if len(vector) >= size:
            print("Vector is already full")
        else:
            addElement = int(input("Type the element to be added: "))
            vector.append(addElement)
    elif option == "2":
        deleteIndex = int(input("Type the index of the element to be deleted: "))
        if len(vector) <= deleteIndex or deleteIndex < 0:
            print("Index doesn't exist")
        else:
            vector.pop(deleteIndex)
    elif option == "3":
        print(vector)
    elif option == "4":
        countNumber = int(input("Type the number to be counted: "))
        counter = 0
        for number in vector:
            if number == countNumber:
                counter += 1
        print(f"The number {countNumber} is in the vector {counter} times")
    elif option == "5":
        if len(vector) == 0:
            print("No elements in the vector")
        else:
            sumVector = 0
            maxVector = -1
            for number in vector:
                sumVector += number
                if number > maxVector:
                    maxVector = number
            meanVector = sumVector / len(vector)
            print(f"The max number is {maxVector} and the mean is {meanVector}")
    else:
        print("Option not valid")