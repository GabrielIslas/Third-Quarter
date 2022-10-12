sign = lambda x: "+" if x > 0 else "-" if x < 0 else "0"

number = float(input("Type a number: "))
print(sign(number))