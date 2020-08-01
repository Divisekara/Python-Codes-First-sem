x=2500
i=1
c=0
while x>i:
    i=i+1
    if x%i==0:
        x=x/i
        answer=i
        if x==1 or x<=i:
            c=1
            break
    if c==1:
        break
print answer
