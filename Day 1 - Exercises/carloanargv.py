from sys import argv

script, P, Y, R = argv 

P = float(P)
Y = float(Y)
R = float(R)

r = R/(12*100)
n = 12*Y

print((P*r)/(1-(1+r)**-n))