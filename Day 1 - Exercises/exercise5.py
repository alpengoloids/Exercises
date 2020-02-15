while True:
    fibci = [0, 1]
    ctr = 1
    y=0
    x = int(input("Input a number: "))
    if x < 1:
        print("NOT A VALID NUMBER OF THIS EXERCISE! EXITING...")
        break
        #continue
    elif x == 1:
        print(fibci[0])
    elif x == 2:
        print(fibci[1])
        print(fibci)
    elif x > 2:
        for y in range(x):
                nfibci=fibci[ctr-1] + fibci[ctr]
                fibci.append(nfibci)
                if len(fibci) != x:
                    ctr += 1
                else:
                    break
        print("The Fibonacci Number for sequence %d is: %d" % (x, fibci[x - 1]))
        print(fibci)


