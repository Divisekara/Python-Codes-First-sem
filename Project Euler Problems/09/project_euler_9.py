"""
for a in range(300):
    for b in range(400):
        c=(a*a+b*b)**0.5
        d=a+b+c
        if d==1000:
            break
    if d==1000:
        break
print a," ",b," ",c
print a*b*c
"""


for a in range (1,1000):
    for b in range(1,1000):
        c=1000-(a+b)
        if (a<b) and (b<c):
            if a**2+b**2==c**2:
                print a," ",b," ",c
                print a*b*c
            
       
        
        
    
