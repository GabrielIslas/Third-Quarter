try:
    x = int(input("Type an integer number: "))
except ValueError:
    print("Error: Not an integer")
    exit()
if x % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")