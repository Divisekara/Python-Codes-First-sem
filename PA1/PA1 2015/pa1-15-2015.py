while True:
    try:
        n=int(raw_input("Enter number: "))
    except ValueError:
        print "Enter integrs only."
        continue
    else:
        sum_=0
        for i in range (1,n+1):
            if n%i==0:
                sum_ += i

        if sum_<2*n:
            print "%s is deficient by %s" %(n,2*n-sum_)
        elif sum_==2*n:
            print "%s is perfect" %(n)
        else:
            print "%s is abundant by %s" %(n,sum_-2*n)

    finally:
        print ""
