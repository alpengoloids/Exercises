str1 = input("Input 1st complete name: ").lower()
str2 = input("Inpunt 2nd complete name: ").lower()

nstr1 = str1.replace(" ", "").lower().replace(".", "")
nstr2 = str2.replace(" ", "").lower().replace(".", "")

for i in str1:
    nstr2 = nstr2.replace(i,"")

for ii in str2:
    nstr1 = nstr1.replace(ii,"")

print(nstr1)
print(nstr2)

total = len(nstr1+nstr2)
print(total)

# F L A M E S

if total == 0:
    print("NULL")
elif total % 6 == 1:
    print("FRIENDS")
elif total % 6 == 2:
    print("L")
elif total % 6 == 3:
    print("A")
elif total % 6 == 4:
    print("M")
elif total % 6 == 5:
    print("E")
elif total % 6 == 0:
    print("S")