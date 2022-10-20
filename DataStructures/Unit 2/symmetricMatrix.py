rows = int(input("Type the amount of rows: "))
columns = int(input("Type the amount of columns: "))

if not rows == columns:
    print("Not symmetric")
else:
    isSymmetric = True
    newArray = [[] for x in range(rows)]
    for i in range(rows):
        for j in range(columns):
            element = input(f"Type element {i}, {j}: ")
            newArray[i].append(element)
    for i in range(rows):
        for j in range(columns):
            if not newArray[i][j] == newArray[j][i]:
                isSymmetric = False
                break;
        if(not isSymmetric):
            break;
    if(not isSymmetric):
        print("Not symmetric")
    else:
        print("Symmetric")
        for i in range(rows):
            print(newArray[i])




    

