a = int(input("Enter a number: "))
b = int(input("Enter another number to be added to the first: "))
c = input("Do you want to + or - these numbers?: ")

if c == "+":
    print(a + b)

elif c == "-":
    print(a - b)

else:
    print("You need to enter either + or -")