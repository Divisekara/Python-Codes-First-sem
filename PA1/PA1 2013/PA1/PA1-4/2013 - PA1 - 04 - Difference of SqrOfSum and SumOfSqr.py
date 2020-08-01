#PA1 - 4 - Difference of SqrOfSum and SumOfSqr

def SqrOfSum(x):
    Sum=0
    for i in range(1,x+1):
        Sum+=i
    return Sum**2

def SumOfSqr(x):
    Sum=0
    for i in range(1,x+1):
        Sum+=i**2
    return Sum

print "Welcome to the SqrOfSum and SumOfSqr Difference Generator!"
a=1
while (a):
    try:
        n = int(raw_input("Enter an integer n where 0<n<100: "))
    except ValueError:
        print "Invalid Input! Enter numerical integer values only."
        continue
    else:
        if n==-1:
            a=0
            print "Good Bye!"
            continue
        elif n<=0 or n>=100:
            print "Invalid Input! Enter integer values inbetween 0 and 100."
        else:
            print "Answer =",abs(SqrOfSum(n)-SumOfSqr(n)),"\n"
