
cnt=0
l=[]

for n in range(1,10):
    while True:
        if n%2==0:
            r=n/2
            n=r
            cnt+=1
        elif n%2!=0:
            r=3*n+1
            n=r
            cnt+=1
        elif r==1:
            break
        l=l+[cnt]
print max(l)
        
        
    
        
        
    
