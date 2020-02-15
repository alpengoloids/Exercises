commodities = ["Sensodyne-100,Close Up-150,Colgate-135","Safeguard-80, Protex-50, Kojic-135","Surf-280, Ariel-350, Tide-635","Clover-60, Piatos-20, Chippy-35","Jelly bean-60, Hany-20, Starr-35"]

brand = []
cheapest = []
total = 0

for producttype in commodities:
	brand.append(producttype.split(","))
#print("Brands per product type: ", brand)

for items in brand:
	lowestprice = 1000
	lowestitem = ""
	for item in items:
		y = item.split("-")
		#print(y)
		if (lowestprice > int(y[1])):
			lowestprice = int(y[1])
			lowestitem = y
		else: 
			continue
	cheapest.append(lowestitem)
	total += int(lowestprice)

cheapest = ','.join(map(str, cheapest)) 
print("Cheapest: ",cheapest)
print("Total: ",total)



	#c = b.split(",")
	#print(c)
