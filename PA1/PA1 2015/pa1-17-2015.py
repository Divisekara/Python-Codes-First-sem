while True:
    try:        
        n=int(raw_input("Enter number: "))
    except ValueError:
        print "Enter numerical positive integers only."
    else:
        if n==-1:
            print "Bye!"
            break
        if not 1<=n<=20:
            print "Enter positive integer between 1 and 20."
            continue

        sum_ = n**3-(n-1)*n
        start = sum_/n
        L=[]

        for i in range(0,n):
            L.append(start+2*i)
        print "Odd number sequence: " + " + ".join(map(str,L))
    finally:
        print ""

