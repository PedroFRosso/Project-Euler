zQ=0
dQ=0

for i in range(101):
    zQ=zQ+i**2
    dQ=dQ+i

dQ=dQ**2
print("Die Differenz ist:", (dQ-zQ))
