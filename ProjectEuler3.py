MAX=600851475143


def prim(x):
    p=[]
    for i in range(1, x+1):
        if x%i==0:
            p=p+[i]
            if sum(p)>(1+x):
                return(x, "ist keine Primzahl")
        if sum(p)==(1+x):
            return(x, "ist Primzahl")
