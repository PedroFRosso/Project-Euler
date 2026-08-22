x=[1, 2]

while x[-1]<4000001:
    x.append(x[-1]+x[-2])

if x[-1]>4000000:
    x=x[0:-1]
print(x)

summe=0
for i in range(len(x)):
    if x[i]%2==0:
        summe=summe+x[i]
print(summe)
