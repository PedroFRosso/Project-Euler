def zT(x):
    p=[]
    e=x//100000
    z=(x-100000*e)//10000
    d=(x-100000*e-10000*z)//1000
    v=(x-100000*e-10000*z-1000*d)//100
    l=(x-100000*e-10000*z-1000*d-100*v)//10
    o=(x-100000*e-10000*z-1000*d-100*v-l*10)
    p=[e]+[z]+[d]+[v]+[l]+[o]
    return(p)

p=[]
stop=False
for i in range(1000000, 100000, -1):
    if zT(i)[0:3]==([zT(i)[-1]]+[zT(i)[-2]]+[zT(i)[-3]]):
        for j in range(1000, 100, -1):
            if i%j==0 and 100<=i/j<1000:
                print(i, j, i/j)
                stop=True
                break
    if stop:
        break

