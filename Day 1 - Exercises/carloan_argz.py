from sys import argv

script, P, Y, R = argv


P = float(P)
Y = float(Y)
R = float(R)

n = Y*12
r = (R/(12*100))

print(argv)

payment = (P*r) / (1-(1+r)**-n)
print("Pay Monthly Amortization amounting to PHP %.2f" % (payment))

argv.reverse()
print(argv)

print(argv[3], argv[1])