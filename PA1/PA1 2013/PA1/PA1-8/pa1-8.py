while True:
    try:
        n=raw_input("Enter the list:")
        L_1=n.split()
        L_2=[]
        L_3=[]
        for i in L_1:
            if int(i)==-1:
                break
            L_2.append(int(i))           
    except ValueError:
        print "Invalid Input. Enter nummerical integers only.\n"      
    else:
        if len(L_1)<7 or len(L_1)>=50:
            print "Enter 7 to 50 amount of numbers only.\n"
        else:
            for j in L_2:
                L_3.append(j) # using another for loop to define L_3 because of same object
                              # is used for L_2 and L_3 otherwise
            max_l=[]
            min_l=[]
            for j in range(3):
                max_l.append(max(L_2))
                L_2.remove(max(L_2))
            for k in range(3):
                min_l.append(min(L_2))
                L_2.remove(min(L_2))
            for m in range(3):
                L_3.insert(L_3.index(max_l[m]),min_l[m])
                L_3.insert(L_3.index(min_l[m]),max_l[m])
                L_3.pop(L_3.index(max_l[m])+1)
                L_3.pop(L_3.index(min_l[m])+1)

            print ' '.join(map(str,L_3))
            
            while True:
                like=raw_input("Do you want to continue (y/n)?:")
                if like=='y':
                    break
                elif like=='n':       
                    break
                else:
                    print "Enter y or n.\n"
            if like=='n':
                break
            
"1 4 7 2 3 5 8 9 10 12 15 -1"
