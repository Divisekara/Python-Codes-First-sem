try:
    w1=list(raw_input("Enter word 1: "))
    w2=list(raw_input("Enter word 2: "))
    w3=list(raw_input("Enter word 3: "))

    index_list_1=[]
    index_list_3=[]
    for i in w1:
        index_list_1.append(w1.index(i))
        for j in w3:
            if i==j:
                index_list_3.append(w3.index(j))
                break
            
    a=0
    if len(index_list_1)==len(index_list_3):
        a=1
        for k in range (len(index_list_3)-1):
            if abs(index_list_3[k]-index_list_3[k+1])!=1:
                a=2
                break

    print index_list_1,index_list_3

    index_list_2=[]
    index_list_3=[]
    for l in w2:
        index_list_2.append(w2.index(l))
        for m in w3:
            if l==m:
                index_list_3.append(w3.index(m))
                break
            
    b=0
    if len(index_list_2)==len(index_list_3):
        b=1
        for k in range (len(index_list_3)-1):
            if abs(index_list_3[k]-index_list_3[k+1])!=1:
                b=2
                break
    print index_list_2,index_list_3

    print a,b
    if a==1 and b==1: print "NOT A SHUFFLE"
    elif a==2 or b==2: print "SHUFFLE"
    else: print "NOTHING"

except:
    print "something went wrong.Try again with a difference."

          
    """
    joy
    enable
    ksjdotiyejnshaqwbolpe
    """
