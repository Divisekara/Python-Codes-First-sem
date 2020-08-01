a=1
while (a):
    try:
        word=str(raw_input("Enter a word:"))
    except ValueError:
        print "Invalid Input. Enter a string format word."   
    else:
        if word=='0':
            a=1
            print "Program Terminated. Good Bye.!"
            break        
        L=list(word)
        c=1
        for i in L:
            if i==' ' or i.isdigit()==True:
                print "Invalid Input. Spaces or integers are not allowed as inputs.\n"
                c=0
                break
        if c==0:
            continue        
        if len(L)%2==1:
            L.pop((len(L)-1)/2)
        L_first = L[0 : len(L)/2]
        L_last  = L[len(L)/2 : len(L)]
        b=0
        for j in L_first:
            for k in L_last:
                if j==k:
                    b=1
                    break
            else:
                b=2
                break
        if b==1:
            print "Yes. Lindrome.\n"
        elif b==2 or b==0:
            print "No. Not a Lindrome.\n"
        else:
            continue
            


