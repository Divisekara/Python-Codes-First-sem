#PA1 - 10 - List Partitioning

a = 1
while (a):
    try:
        N = raw_input("Enter the Sequence Sn (where 10<=n<=100): ").split()
        Sn = []
        for i in N:
            if int(i)==-1:
                break
            else:
                Sn.append(int(i))
        k = int(raw_input("Enter k (where 1<=k<=n): "))
        if len(Sn)<10 or len(Sn)>100:
            print "Invalid Input! Enter the sequence Sn within the given range"
        elif k<1 or k>len(Sn):
            print "Invalid Input! Enter integer k inbetween the given range"
    except ValueError:
        print "Invalid Input! Enter numerical integer values."
        continue
    else:
        m = Sn[k-1]
        Sn2=[]
        i=0
        while i<len(Sn)-1:
            if m<Sn[i]:
                Sn2.append(Sn.pop(Sn.index(Sn[i])))
            i+=1
        Sn.sort()
        Sn2.sort()
        print "Partition Sn1:"," ".join(map(str,Sn))
        print "Partition Sn2:"," ".join(map(str,Sn2)),"\n"
