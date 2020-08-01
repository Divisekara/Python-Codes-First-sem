def d(n):
    sum_=0
    for i in range(1,n):
        if n%i==0:
            sum_+=i
    return sum_



sum_2=0
n=1
while n<10000:
    
    if d(d(n))==n and d(n)!=n:
        sum_2=sum_2+n
    n+=1
print sum_2
#40284
