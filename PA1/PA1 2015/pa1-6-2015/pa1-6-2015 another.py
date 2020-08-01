def weight(L):

    alpha=map(ord,L)
    for j in alpha:
        if j<97:
            alpha[alpha.index(j)]=j+32
    for k in alpha:
        alpha[alpha.index(k)]=k-96
    weight=0
    n=1
    for i in alpha:
        weight += (i)*n
        n=n+1
    return weight


x=raw_input("Enter the input word:")

for i in range(0,len(x)):
    left=x[0:i-1]
    right=x[i:]

    if weight(left)==weight(right):
        print "Balance point letter: '%s', weight=%s" %(x[i-1],weight(left))
        break
else:
    print "cannot be balenced!"
    
