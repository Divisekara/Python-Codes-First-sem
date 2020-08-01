a=1
while (a):
    try:
        n=int(raw_input("Enter number:"))
    except ValueError:
        print "Enter numerical positive integers only between 0 and 50."
        continue
    except:
        print "Something went wrong.Try again with a different input."
        continue
    else:
        if not 0<n<50:
            print "Invalid Input. Enter positive integer between 0 and 50."
            continue
        elif n==-1:
            print "Good bye. Programme terminated."
            a=0
            break
        else:
            for i in range(1,n+1):
                line=""
                for j in range(n-i):
                    line+=" "*4
                for k in range(-i,i+1):
                    if k==-1 or k==0:
                        continue
                    else:
                        line+="%4s" % abs(k)
                print line
    finally:
        print "\n"
        
            
    
