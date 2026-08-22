d={0: 2, 1: 3}
def primfinder(x):
    for i in range(len(d)):
        if x%d[i]==0:
            return 
    d.update({len(d): x})
    return 

s=4
while not len(d)==10001:
    primfinder(s)
    s=s+1

print(d.get(10000))