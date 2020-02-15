stringlist = ["Sensodyne-100,Close Up-150,Colgate-135", "Safeguard-80,Protex-50,Kojic-135",
              "Surf-280,Ariel-250,Tide-635", "Clover-60,Piatos-20,Chippy-35", "JellyBean-60,Hany-20,Starr-35"]

catgry = []
output = ""
total = 0

print(stringlist)

# toothpaste = stringlist[0].split(",")
# print(toothpaste)

for x in stringlist:
    catgry.append(x.split(","))
print(catgry)

for products in catgry:
    flag = True
    cheapProdName = ""
    cheapProdPrice = 0
    for brand in products:
        item = brand.split("-")
        if flag:
            cheapProdName = item[0]
            cheapProdPrice = float(item[1])
            flag = False
        else:
            if float(item[1]) < cheapProdPrice:
                cheapProdName = item[0]
                cheapProdPrice = float(item[1])

    output = output + cheapProdName + "-" + str(cheapProdPrice) + ","
    total = total + cheapProdPrice

print("Cheapest: " + output[0:-2])
print("Total: " + str(total))

"""
for ii in range(len(catgry[0])):
    item = catgry[ii][ii].split("-")
    prices = item[1]



a = catgry[0][0].split("-")
b = a[1]

print(a)
print(b)
"""
