'''2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20 ?
'''

i=2520
list_check=[11,13,14,16,17,18,19]

while i>19:
    n=0
    for j in (list_check):
        if i%j==0:
            n=n+1
        else:
            i=i+2520
            break
    if n==7:
        print i ,"is the answer."        
        break
    else:
        continue
    
    
"""

Python

from functools import reduce

def gcd(a, b):
    #Return greatest common divisor using Euclids Algorithm.
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    #Return lowest common multiple.
    return a * b // gcd(a, b)

def lcmm(*args):
    #Return lcm of args.
    return reduce(lcm, args)

"""

"""

all_nums = list(range(2,21))

ans = 1

while all_nums:
     head = all_nums[0]
     for i,j in enumerate(all_nums):
         if j % head == 0:
             all_nums[i] //= head
     all_nums = list(filter(lambda x: x != 1,all_nums))
     ans *= head
print(ans)


"""


"""

from functools import reduce
def HCF(x,y):
    while y:
        x,y=y,x%y
    return x
print(reduce(lambda x,y:(x*y)//HCF(x,y) ,list(range(1,21))))

"""





