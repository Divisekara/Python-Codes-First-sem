#PA1-1 - Products from a Sequence

print "Welcome to the Sequence Products Generator!"
a=1
while (a):
    try:
        n = raw_input("Enter an integer n with m digits and 0<m<9: ")
        m = len(n)
        p = int(n)
    except ValueError:
        print "Invalid Input! Enter numerical integer values only."
        continue
    else:
        if n=="-1":
            a=0
            print "Good Bye!"
            continue
        elif m<=2 or m>=9 or n<0:
            print "Invalid Input! Enter an interger between 100 and 100,000,000."
            continue
        else:
            for i in n:
                if i=="0":
                    print "Enter an integer which does not contain the digit 0"
                    break
                continue
            product = 1
            for j in n:
                for k in n:
                    if k!=j:
                        product*=int(k)
                print product,
                product = 1
            print "\n"

            #for j in n:
                #product*=int(j)
            #for k in n:
                #print product/int(k),
            #print "/n"
            
            
