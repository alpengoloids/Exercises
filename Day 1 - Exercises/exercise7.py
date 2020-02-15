x=float(input("Input amount: "))
y=float(input("Enter conversion rate (1USD to PHP): "))

while True:
    print("\n")
    print("[A/a] USD to PHP")
    print("[B/b] PHP to USD")

    z=input("Please select character: ")

    if z == 'a' or z == "A":
        answr = (x/y)
        print("\n")
        print("%d PHP is equal to %.2fUSD" % (x, answr))
        break
    elif z == 'b' or z == 'B':
        answr=(x*y)
        print("\n")
        print("%d USD is equal to %.2f PHP" % (x,answr))
        break