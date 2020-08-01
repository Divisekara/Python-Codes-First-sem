ans=0
for a in range(100,1000):
    for b in range (100,1000):
        x=a*b
        y=str(x)

        L=[]

        for i in (y):
            L.append(i)

        M=[]

        for j in (L):
            M.append(j)

        M.reverse()

        if L==M:
            if ans<x:
                ans=x
                print ans,'=',a,'x',b
