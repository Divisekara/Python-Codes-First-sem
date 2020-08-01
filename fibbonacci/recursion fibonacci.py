##def function(n):
##    if n==0 or n==1:
##        return 1
##    else:
##        return function(n-1)+ function(n-2)


def function(n):
    if n==0 or n==1:
        return 1
    return function(n-1)+ function(n-2)


for i in range(10):
    print function(i)
