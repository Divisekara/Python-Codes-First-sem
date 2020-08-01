while True:
    try:
        n=int(raw_input("Enter N (Size of matrix):"))
        print "Enter the Matrix:"
        L=[]
        a=0
        for i in range(n):
            L.append(raw_input().split())
            if len(L[i])!=n:
                print "Enter correct amount of items for a row."
                a=1
                break
        if a==1:continue
        L_up=[]
        L_dn=[]
        for j in range(0,n):             # locating rows
            for k in range(n-1,j,-1):    L_up.append(L[j][k])
            for l in range(0,j):         L_dn.append(L[j][l])
        answer_up=0
        answer_dn=0
        for m in L_up:
            if int(m)==0:answer_up=2
            else:break
        for p in L_dn:
            if int(p)==0:answer_dn=1
            else:break
    except ValueError:
        print "Enter positive Integers only."
        continue
    else:
        if not 0<=n<=8:
            print "Enter N  between 1 and 8."
            continue       
        else:        
            if answer_up==2 and answer_dn==1:print "Answer:3"
            elif answer_up==2:               print "Answer:%s" %answer_up
            elif answer_dn==1:               print "Answer:%s" %answer_dn
            else:                            print "Answer:4"
