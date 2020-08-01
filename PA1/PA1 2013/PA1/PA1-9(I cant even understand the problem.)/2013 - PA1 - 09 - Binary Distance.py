l=input("l :")
m=input("m :")
n=input("n :")
A=[]
A1=[]
B=[]
B1=[]
C=[[]]*l
print C
for i in range(0,m):
    A.append(raw_input().split())
for row in A:
    r=[]
    for e in row:
        r.append(int(e))
    A1.append(r)
print "done1"

for i in range(0,n):
    B.append(raw_input().split())

for row in B:
    r=[]
    for e in row:
        r.append(int(e))
    B1.append(r)
print "done2"
print A1,B1
t=0
for i in range(0,l):
    for j in range(0,n):
        for k in range(0,m):
            t+=A1[i][k]*B1[k][j]
        C[i].append(t)
        print C[i][j]
        t=0
print C    
