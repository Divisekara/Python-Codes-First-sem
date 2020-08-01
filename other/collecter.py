"""
sum_1=0
sum_2=0
for i in range(1000):
    if i%3==0:
        sum_1+=i
    elif i%5==0:
        sum_2+=i
sum_=sum_1+sum_2
print sum_
"""

"""for i in range(1,20):
    for n in range(2,i):
        if i%n==0:
            break
    else:
        print i"""

             
n=int(raw_input())
is_prime=True
for i in range (2,n):
    if n%i==0:
        is_prime=False
        break
if is_prime==True:
    print n ' is a prime
    


