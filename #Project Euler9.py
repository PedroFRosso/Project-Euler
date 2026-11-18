quadrate={}

i=1
while i <= 1000:
    quadrate.update({i: i**2})
    i+=1

for a in range(1, 1000):
    for b in range(1, 1000):
        if a**2+b**2 in quadrate:
            print (a, b, quadrate[a**2+b**2])
        if a+b+(a**2+b**2)**0.5 ==1000:
            print("Hier", a, b, (a**2+b**2)**0.5)
            print(a*b*(a**2+b**2)**0.5)
            break