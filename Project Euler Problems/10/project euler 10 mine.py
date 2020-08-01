n=2
sum_prime=0

while n<2000000:
    is_prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            break

    if is_prime==True:
        sum_prime=sum_prime+n

    n=n+1

print sum_prime
print n        
        
