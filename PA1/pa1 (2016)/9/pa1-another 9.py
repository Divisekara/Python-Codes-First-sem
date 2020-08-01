while True:
    try:        
        n=int(raw_input("Enter number: "))
    except ValueError:
        print "Invalid Input Enter numerical integers only."
        continue
    else:
        if not 0<=n:
            print "Enter numerical positive integers."
            continue
        L=[[455,33],[11,13],[1,11],[3,7],[11,2],[1,3]]
        times = 0
        while True:
            for i in L:
                p=i
                if (n*p[0])%p[1]==0:
                    n = n*p[0]/p[1]
                    times += 1
                    break
            else: break
        print times , n
    finally:
        print ""
            
        
            





