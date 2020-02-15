from sys import argv

script, x = argv

x=float(x)

if x == 50 or x == -50 or x == 0:
  print("Border")

elif x > 50 or x < -50:
  print("Out of Range")

elif x >= 1 and x <= 49:
  print("Positive Range")

elif x <= -1 and x >= -49:
  print("Negative Range")