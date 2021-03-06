while True:
    print("[1] EXERCISE 1: IDENTIFYING LEAP YEAR")
    print("[2] EXERCISE 2: GRADES CONVERSION")
    print("[3] EXERCISE 3: SIMPLE CALCULATOR")
    print("[4] EXERCISE 4: EXPONENTIATION")
    print("[5] EXERCISE 5: FIBONACCI PROGRAM")
    print("[6] EXERCISE 6: WORKING WITH LISTS")
    print("[7] EXERCISE 7: USD <> PHP CONVERSION")
    print("[x] TO EXIT")
    print("\n")
    select = input("Please select Exercise: ")
    print("\n")

    if select == '1':
        print("EXERCISE 1: Identify if a given year is a Leap or not.")
        while True:
            yrz = int(input("Enter a year (XXXX): "))
            if yrz >= 1 and yrz <= 9999:
                if yrz % 4 == 0:
                    if yrz % 100 == 0:
                        if yrz % 400 == 0:
                            print("%d is a LEAP YEAR!" % yrz)
                        else:
                            print("%d is NOT a Leap Year" % yrz)
                    else:
                        print("%d is a LEAP YEAR!" % yrz)
                else:
                    print("%d is NOT a Leap Year" % yrz)
            print("\n")
            break

            yrz = 0

    elif select == '2':
        grade = 0
        while True:
            print("EXERCISE 2: Converting Number Grading to Letter Grading: ")
            grade = int(input("Enter a grade: "))
            if grade <= 100:
                if grade <= 100 and grade >= 90:
                    print("Grade: A")
                    break
                elif grade < 90 and grade >= 80:
                    print("Grade: B")
                    break
                elif grade < 80 and grade >= 70:
                    print("Grade: C")
                    break
                elif grade < 70 and grade >= 60:
                    print("Grade: D")
                    break
                else:
                    print("Grade: E")
                    break

    elif select == '3':
        print("EXERCISE 3: Simple Calculator")
        x = float(input("Input 1st number: "))
        y = float(input("Input 2nd Number: "))

        while True:
            print("\n")
            print("[A/a] FOR ADDITION")
            print("[B/b] FOR SUBTRACTION")
            print("[C/c] FOR MULTIPLICATION")
            print('[D/d] FOR DIVISION')
            print("\n")
            z = input("Please select operation: ")

            if z == 'a' or z == "A":
                print("Summation of %d and %d is: " % (x, y))
                print(x + y)
                break
            elif z == 'b' or z == 'B':
                print("Difference of %d and %d is: " % (x, y))
                print(x - y)
                break
            elif z == 'c' or z == 'C':
                print("Product of %d and %d is: " % (x, y))
                print(x * y)
                break
            elif z == 'd' or z == 'D':
                print("Quotient of %d and %d is: " % (x, y))
                print(x / y)
                break

    elif select == '4':
        print("EXERCISE 4: Raising number to nth power")
        n = int(input("Input Integer: "))
        p = int(input("Input Exponent: "))
        print("%d raised to exponent %d is : %d" % (n, p, n ** p))
        continue

    elif select == '5':
        print("EXERCISE 5: Finding nth Fibonacci Number")
        while True:
            fibci = [0, 1]
            ctr = 1
            y = 0
            x = int(input("Input a number: "))
            if x < 1:
                print("NOT A VALID NUMBER FOR THIS EXERCISE! EXITING...")
                break
                # continue
            elif x == 1:
                print(fibci[0])
            elif x == 2:
                print(fibci[1])
                print(fibci)
            elif x > 2:
                for y in range(x):
                    nfibci = fibci[ctr - 1] + fibci[ctr]
                    fibci.append(nfibci)
                    if len(fibci) != x:
                        ctr += 1
                    else:
                        break
                print("The %dth Fibonacci Number is: %d" % (x, fibci[x - 1]))
                print(fibci)
            break

    elif select == '6':
        print("EXERCISE 6: Working with Lists")
        import random

        randlist = []

        for i in range(20):
            n = random.randint(1, 999)
            randlist.append(n)

        print(randlist)
        print("\n")

        while True:
            z = input("Convert all EVEN Numbers to ODD Numbers? [Y/y] ")
            if z == 'y' or z == "Y":
                print("New List below: ")
                for ii in range(len(randlist)):
                    if randlist[ii] % 2 == 0:
                        randlist[ii] = randlist[ii] + 1
                # print("\n")
                print(randlist)
                break

    elif select == '7':
        print("EXERCISE 7: USD <> PHP Conversion:")
        x = float(input("Input amount: "))
        y = float(input("Enter conversion rate (1USD to PHP): "))

        while True:
            print("\n")
            print("[A/a] USD to PHP")
            print("[B/b] PHP to USD")

            z = input("Please select character: ")

            if z == 'a' or z == "A":
                answr = (x / y)
                print("\n")
                print("%d PHP is equal to %.2fUSD" % (x, answr))
                break
            elif z == 'b' or z == 'B':
                answr = (x * y)
                print("\n")
                print("%d USD is equal to %.2f PHP" % (x, answr))
                break
    print("\n")
    while True:
        choice = input("TRY ANOTHER EXERCISE? Y/N:  ")
        if choice == 'Y' or choice == 'y':
            break
        elif choice == 'N' or choice == 'n':
            print("Exiting Program. Goodbye!")
            exit()

        elif select == 'x':
            print("Exiting Program. Goodbye!")
            break


