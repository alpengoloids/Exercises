myname = input("Enter your name: ")
crushname = input("Enter your crush's name: ")
name1 = myname.lower()
name2 = crushname.lower()

for x in myname.lower():
	name2 = name2.replace(x,"")

for x in crushname.lower():
	name1 = name1.replace(x,"")


name1 = name1.replace(".","")
name2 = name2.replace(".","")
total = len(name1.replace(" ",""))+len(name2.replace(" ",""))

if total%6 == 1:
	print("Friendship")
elif total%6 == 2:
	print("Love")
elif total%6 == 3:
	print("Affection")
elif total%6 == 4:
	print("Marriage")
elif total%6 == 5:
	print("Enemy")
elif total%6 == 6:
	print("Soulmate")
elif total == 0:
	print("Zero parang Lovelife mo.")