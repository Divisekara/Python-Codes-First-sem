while True:
    try:
        sn=raw_input("enter a list of space seperated numbers :")
        k=int(raw_input("Enter k:"))
        L_1=sn.split()
    except ValueError:
        print "Invalid input for k. Enter numerical positive Integers only.\n"
    else:
        a=0
        if len(L_1)<10 or len(L_1)>100:
            print "Enter 10 to 100 amounts of numbers only.\n"
        elif 1<=k<=len(L_1):          
            L_2=[]
            sn_1=[]
            sn_2=[]
            try:     
                for i in L_1:
                    if int(i)==-1:
                        break
                    elif int(i)<-1:
                        print "Positive Integers only are valid as input.\n"
                        a=1
                        break
                    else:
                        L_2.append(i)
            except ValueError:
                print "Invalid input for list. Enter numerical positive Integers only.\n"
            else:
                if a==1:
                    pass
                else:
                    for j in L_2:
                        if int(j)>int(L_2[k-1]):
                            sn_2.append(j)
                        else:
                            sn_1.append(j)

                    print "First partition Sn1= " + " ".join(map(str,sn_1))
                    print "Second partition Sn2= " + " ".join(map(str,sn_2))
                    print "\n"
        else:
            print "Enter k within 1<=k<=length of list.\n"
"30 15 36 12 34 96 11 4 5 7 -1"
