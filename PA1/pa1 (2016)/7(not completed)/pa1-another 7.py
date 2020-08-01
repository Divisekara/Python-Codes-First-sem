lhs = raw_input("Left hand side: ").upper().split("+")
D1={}

for i in lhs:
    b=list(i)
    b.remove("*")
    c=1
    E=""
    
    for j in b:
        if j.isdigit()==True:
            c *= int(j)
        if j.isalpha()==True:
            E = j
    #D[E]=c
    D1.update({E:c})
      
rhs = raw_input("Left hand side: ").upper().split("*")

c=int(rhs[0])
b=list(rhs[1])
num=[]
elem=[]
for k in b:
    if k.isalpha()==True:
        elem.append(k)

    if k.isdigit()==True:
        num.append(int(k)*c)

D2={} 
for i in range(0,len(elem)):
    D2.update({elem[i]:num[i]})

print D1==D2

"""
if (sorted(D1)==sorted(D2))==True:
    print "Correct"
else:
    print "Incorrect"
"""
print D1,D2


