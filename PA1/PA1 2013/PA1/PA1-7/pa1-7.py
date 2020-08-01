while True:
    try:    
        n=int(raw_input("Enter a number:"))
    except ValueError:
        print "Inavlid Input. Enter numerical value integers."
    else:
        if n==-1:
            print "Good Bye. Program terminated."
            break
        elif n<-1:
            print "Enter positive Integers between 0 and 88."
        elif 1<n<=88:
            L=list(str(n))
            num_add=0
            if L==L[::-1]:
                palindrome=n
                num_add=0

            else:
                while L!=L[::-1]:
                    n=int(''.join(L))+int(''.join(L[::-1]))
                    L=list(str(n))
                    palindrome=n
                    num_add=num_add+1
                            
                    
            print "palindrome=" + str(palindrome) + ", number of addition=" + str(num_add)
    
        else:
            print "Enter integer bettween 1 and 88."
            
    print '\n'

