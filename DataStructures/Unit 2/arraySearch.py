import numpy as np # array library
newArray = np.array([1, 2, 3], dtype=int) # creating new array
print(newArray) # printing
x = np.where(newArray ==  2)
print(x) # printing new array