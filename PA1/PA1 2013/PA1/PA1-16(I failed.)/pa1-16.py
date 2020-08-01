def dec_bin(dec):
    L=list(bin(dec))
    L=L[2:]
    return L

a=1
while (a):
    try:    
        n=int(raw_input("Enter number:"))
    except ValueError:
        print "Invalid Input.Enter numerical postive integers only.\n"
    except:
        print "Something went wrong. Try again with another input.\n"
    else:
        if n>0:
            digit=[]
            digit=dec_bin(n)
            a=digit.count('1')

            while True:
                n=n+1
                if a==dec_bin(n).count('1'):
                    break
            print "The answer:",n ,"\n"
        else:
            print "Invalid Input.Enter positive integers only.\n"

    finally:
        print "\n"
            
        

