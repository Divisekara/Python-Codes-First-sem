a,b=1,2
sum_=0
while b<4000000:
    c=a+b
    a,b=b,c
    if c%2==0:     
        sum_=sum_+c
print sum_    
