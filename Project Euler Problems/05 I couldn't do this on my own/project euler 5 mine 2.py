def gcd(a,b):
    while b:
        a , b = b , a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

a=1

for i in range(1,21):
    x=lcm(a,i)
    a=x
print x
