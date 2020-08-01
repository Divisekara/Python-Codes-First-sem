while True:
    try:
        n=list(raw_input())
        L=[]

        for i in range(1,len(n)):
            prefix=int("".join(n[0:-i]))
            if prefix%4==0:
                L.append(prefix)
            
    except ValueError:
        print "Enter integers only"
        
    else:
        print "Posiible prefixes: " +", ".join(map(str,L))

    finally:
        print ""



