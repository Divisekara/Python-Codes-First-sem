def average(L):
    sum_=0
    for i in L:
        sum_+=float(i)
    average=sum_/len(L)
    return average

try:
    L=raw_input("Input stock prices of the week: ").split()
    value=average(L)+10
except ValueError:
    print "Invalid input. Enter numerical values only."
else:
    n=0
    for i in L:
        if float(i)>value:
            n=n+1         
    print "Number of valued days: %s" %(n)
    if n==3:
        print "RECOMMENDED"
    else:
        print "NOT RECOMMENDED"

finally:
    print "\n"


"70.5 78.9 90.7 33.2 56.0 40.2 22.1"
"33.5 46.9 40.7 43.2 26.0 30.2 32.1"
