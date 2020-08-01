d=1
c=1

for b in range(1,1000):
    
    for a in range(1,b):
        c=(a**2 + b**2)**0.5
        
        if a+b+c==1000:
            d=1000
            break

    if d==1000:
        break


print a , b , c
print a*b*c 
