S,T=0,0
for r in range(1,104):
    T=float(3)/float(r)*float(2-r)**float(3)
    S=S+T
    print r,T
print 'total is ',S
