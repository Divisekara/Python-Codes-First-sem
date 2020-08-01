#fibonnaci series

"""a=1
sum_=0
for i in range(10):
    sum_=sum_+a
    a,sum_=sum_
    print sum_"""

#how to interchange two values of variables a,b=b,a

a,b=1,1
while a<100:
    a,b=b,a+b  # we cant do these two operatons in two lines
    print a
    
