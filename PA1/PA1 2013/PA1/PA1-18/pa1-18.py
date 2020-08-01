a=1
while (a):
    try:
        l=raw_input("Enter the input number list by seperated space: ").split()
        just=list(map(int,l))

    except ValueError:
        print "Invalid input.Enter numerical integers only.\n"

    except:
        print "Something went wrong.Try again with another input.\n"

    else:  
        D1={}
        D2={}
        sum_=[]
        n=[]
        for q in l:
            n.append(q)
            if int(q)==-1:
                break

        for i in n:
            if n.count(i)>=2:
                if (i in D1)==False:
                    D1.update({i:n.index(i)+1})
                    sum_.append(i)

                else:
                    m=[]
                    for j in n[n.index(i)+1:]:
                        m.append(j)
                    D2.update({i:m.index(i)+n.index(i)+2})

        p=1
        if len(D1)>0:
            for k in D1:
                print "Duplicate number %s = %s, Position %s and %s" %(p,k,D1[k],D2[k])
                p+=1
            print "Sum of the duplicate number = %s" %(sum(map(int,D1)))
        else:print "No duplicate numbers"
    finally:
        print "\n"
    
