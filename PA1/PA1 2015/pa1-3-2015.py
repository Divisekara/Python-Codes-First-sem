print "Knockout information generater - Tennis tourament."
try:
    p=int(raw_input("Enter number of players, p: "))
except ValueError:
    print "Invalid input enter positive integers only."
except:
    print "something went wrong. Try again witha a difference."
else:
    round_=0
    matches=0
    n=p
    m=1
    while m<=n:
        m*=2
    m/=2

    while n>=2:
        round_+=1
        matches+=m/2
        n=n-m/2
        if n>=m:
            pass
        else:
            m=m/2
        

    print "Number of rounds=%s, matches=%s " %(round_, matches)   



        
