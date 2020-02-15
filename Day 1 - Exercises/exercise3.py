x=float(input("Input 1st number: "))
y=float(input("Input 2nd Number: "))

while True:
    print("\n")
    print("[A/a] FOR ADDITION")
    print("[B/b] FOR SUBTRACTION")
    print("[C/c] FOR MULTIPLICATION")
    print('[D/d] FOR MULTIPLICATION')
    print("\n")
    z=input("Please select operation: ")

    if z == 'a' or z == "A":
        print("Summation of %d and %d is: " % (x,y))
        print(x+y)
        break
    elif z == 'b' or z == 'B':
        print("Difference of %d and %d is: " % (x, y))
        print(x-y)
        break
    elif z == 'c' or z == 'C':
        print("Product of %d and %d is: " % (x, y))
        print(x*y)
        break
    elif z == 'd' or z == 'D':
        print("Quotient of %d and %d is: " % (x, y))
        print(x/y)
        break
