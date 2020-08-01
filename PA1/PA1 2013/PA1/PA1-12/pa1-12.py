while True:
    try:   
        n=int(raw_input("Enter a number between 1 to 10:"))
        L=[]
        
        if n<1 or n>=10:
            print "Invalid number of rows. Enter between 1 to 10."
            continue
        
        for i in range(1,n+1):
            row=raw_input("Enter row %s:" %(i)).split()
            L.append(row)

        a=0
        for l in L:
            if len(l)!=3:
                a=1
                break
            for m in l:
                a=int(m)

        if a==1:
            print "Invalid Number of elements in a row.\n"
            continue
        
    except ValueError:
        print "Enter numerical integers only.\n"

    else:
        print "Transepose of the input matrix is:"
        for j in range(0,n):
            for k in range(0,n):
                print L[k][j],
            print ''
        print ''
