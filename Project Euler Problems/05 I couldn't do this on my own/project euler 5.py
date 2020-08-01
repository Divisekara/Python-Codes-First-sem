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
    













