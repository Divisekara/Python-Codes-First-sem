n=0
x=2
while True:
    is_prime=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            is_prime=False
            break
    if is_prime==True:
        n=n+1

    if n==10001:
        print x
        break

    x=x+1
        
            
