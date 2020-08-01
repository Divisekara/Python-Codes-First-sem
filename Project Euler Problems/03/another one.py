x=600851475143
n=2
while n<x:
    while x%n==0:
        x=x/n
        print n
    n=n+1
print n

