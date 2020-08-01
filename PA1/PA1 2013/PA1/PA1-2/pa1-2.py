import sys
while True:
    try:    
        n=int(raw_input("Enter an integer between 1 and 10000: "))
    except ValueError:
        print "Invalid Input. Give a numerical integer\n"
        print sys.exc_info()[0]
    else:
        L=[]
        if n==0:
            print "Program Terminated. Good Bye."
            sys.exit()
        if n<0 or n>10000:
            print "Invalid input. Enter an integer between 1 and 10,000.\n"
            continue      
        while n>0:
            if n%2==0:
                n=n/2
                L.append(0)
            else:
                n=n//2
                L.append(1)
        L.reverse()
        string=''
        for i in L:
            string=string+str(i)
        print string ,'=',
        L.reverse()
        n=0
        for j in L:
            print "{}*2^{}".format(j,n),
            n+=1
            if n<len(L):
                print "+",
    print "\n"


