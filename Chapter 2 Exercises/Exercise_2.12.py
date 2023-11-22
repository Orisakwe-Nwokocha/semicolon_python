p = 1000
r = 0.07
n1 = 10
n2 = 20
n3 = 30

a1 = p * (1 + r) ** n1
a2 = p * (1 + r) ** n2
a3 = p * (1 + r) ** n3

print("%.2f" % a1, "is the amount on deposit at the end of", n1, "years.")
print("%.2f" % a2, "is the amount on deposit at the end of", n2, "years.")
print("%.2f" % a3, "is the amount on deposit at the end of", n3, "years.")