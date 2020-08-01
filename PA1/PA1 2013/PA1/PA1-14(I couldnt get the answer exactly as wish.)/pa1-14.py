while True:
    try:
        n=int(raw_input("Enter n(height of the traingle):"))
    except ValueError:
        print "Enter numerical positive integers only.\n"
    except:
        print "Something went wrong. try again."
    else:
        if not 0<n<50:
            print "Invalid Input. Enter n between 0 and 50.\n"
        else:
            L=[1,2,1]
            L1=[1,2,1]

            for p in range(1,n):
                for l in range(n-p-1):
                    print " ",
                if p==1:
                    print " 1"
                    continue
                else:
                    print "  ".join(map(str,L1))
                    break


            for m in range(1,n):
                L2=[]
                L2.insert(0 , L1[0])
                
                for i in range(1,len(L1)):
                    L2.insert(i , L1[i-1] + L1[i])
                L2.insert(i+1 , L1[0])
                L1=[]
                
                for j in (L2):
                    L1.append(j)

                for k in range(len(L2),n):
                    for l in range(n-k):
                        print " ",
                        
                    print "  ".join(map(str,L2))
                    break
    finally:
        print "\n"

    '''
    L1=[1,2,1]
    L2=[]
    L2.insert(0 , L1[0])
    L2.insert(1 , L1[0] + L1[1])
    L2.insert(2 , L1[1] + L1[2])
    L2.insert(3 , L1[2])
    L1=[]
    for j in (L2):
        L1.append(j)
    print L1
    print L2
    '''
    '''
    L1=[1,3,3,1]
    L2=[]
    L2.insert(0 , L1[0])
    L2.insert(1 , L1[0] + L1[1])
    L2.insert(2 , L1[1] + L1[2])
    L2.insert(3 , L1[2] + L1[3])
    L2.insert(4 , L1[0])
    L1=[]
    for j in (L2):
        L1.append(j)
    print L1
    print L2
    '''
