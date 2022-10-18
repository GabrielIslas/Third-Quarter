# function to add two arrays
def addTwoArrays(arr1, arr2):
    # check dimensions
    if not dimensionCheck(arr1, arr2):
        print("Can't add arrays due to different dimensions")
        return
    arraySum = [[] for x in range(len(arr1))] # initializing space of sum array, add empty rows
    for index1 in range(len(arr1)):
        for index2 in range(len(arr1[0])):
            # fill rows with sum of elements
            arraySum[index1].append(arr1[index1][index2] + arr2[index1][index2])
    return arraySum    
# function to check dimensions
def dimensionCheck(arr1, arr2):
    # same amount of rows
    if len(arr1) != len(arr2):
        return False
    # rows are equal size for both arrays (wouldn't be an array then)
    for row1 in arr1:
        if len(row1) != len(arr1[0]):
            return False
    for row2 in arr2:
        if len(row2) != len(arr2[0]):
            return False
    # checking rows between arrays are the same size
    for row1 in arr1:
        for row2 in arr2:
            if len(row1) != len(row2):
                return False
    return True

# input section of arrays
rows = int(input("Type the amount of rows: "))
columns = int(input("Type the amount of columns: "))
# initializing empty arrays based on row amount
inputArr1 = [[] for x in range(rows)]
inputArr2 = [[] for x in range(rows)]
# adding elements individually
for x in range(rows):
    for y in range(columns):
        arr1Element = int(input(f"Type element {x}, {y} for array 1: " ))
        inputArr1[x].append(arr1Element)
        arr2Element = int(input(f"Type element {x}, {y} for array 2: " ))
        inputArr2[x].append(arr2Element)

print(addTwoArrays(inputArr1, inputArr2))


# test arrays (not input)
array1 = [[1,2,3], [1,4,1], [5,7,3]]
array2 = [[1,2,3], [1,4,1], [5,4,3]]
array3 = [[1,2,3], [1,4,1]]
array4 = [[1,2,3], [5,4,3]]
array5 = [[1,2], [1,3], [1,4]]
array6 = [[1,2], [1,3], [1,8]]


print(addTwoArrays(array3, array5))