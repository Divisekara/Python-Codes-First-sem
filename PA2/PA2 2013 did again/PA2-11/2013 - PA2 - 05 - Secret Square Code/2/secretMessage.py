s="ydrescl oeecscl ucdraey hitegs aphtes vhemsf eeseuu"

L=s.split()

for t in range(len(L)):
    if len(L[t])!=7:
        L[t]+=(7-len(L[t]))*' '

print L
newL=[]

  
for i in range(7):
    q=''
    for w in L:
        q+=w[i]
    newL.append(q)

output=''

for i in newL:
    output+=i+" "

print output
    
