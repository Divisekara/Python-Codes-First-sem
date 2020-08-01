while True:
    try:
        n=int(raw_input("Enter number: "))
    except ValueError:
        print "Enter numerical integers only"
        continue
    else:
        if not 1<=n<10**4:
            print "Enter positive integers between 1 and 10000."
            continue
        rew=1
        for i in range(10,n+1):
            for j in range(2,7):
                if i%j==0:
                    break
            else:
                rew +=1
        print rew
                
    finally:
        print "\n"
