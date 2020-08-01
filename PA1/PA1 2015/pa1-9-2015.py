def check(x):    #input the list of numbers of word 1 to 26
    a=1
    for i in range(0,len(x)):
        for j in range(i,len(x)):
            diff=x[i]-x[j]
            if diff>0:
                a=0
                break
        if a==0:
            break
    if a==0:
        return False
    else:
        return True
        

        
while True:
    word=raw_input().strip()
    if word.isalpha()==False:
        print "Enetr words only."
        continue
    
    x=map(ord,list(word.lower()))

    L=[]
    for i in x:
        L.append(i-96)

    if check(L)==True:
        print word, "IN ORDER"
    else:
        if check(L[::-1])==True:
            print word, "IN REVERSE ORDER"
        else:
            print word, "NOT IN ORDER"
