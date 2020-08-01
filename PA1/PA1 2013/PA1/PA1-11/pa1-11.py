while True:
    try:    
        n=raw_input("Enter two strings with a space:").split()
        L1=n[0]
        L2=n[1]
        a=0
        b=0
        for i in L1:
            if i.isdigit()==True:
                b=1
            for j in L2:
                if j.isdigit()==True:
                    b=1
                elif L1.index(i)==L2.index(j):
                    if i!=j:
                        a=a+1
        if b==1:
            print "Invalid Input.Enter letters only."
            continue        

        a = a + abs(len(L1)-len(L2))
        print a
    except:
        print "Something went wrong. Try with another input."
                        


