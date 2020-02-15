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
    yrz = 0



