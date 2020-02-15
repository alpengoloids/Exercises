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
        print("\n")
        print(randlist)
        break
