import sys

print "Welcome to the sequence products generater"
while True:
    
    try :
        n = str(raw_input("Enter number between 100 and 100,000,000: "))
        m=len(n)

        if int(n)==-1:
            print "Program is over. Good Bye.\n"
            sys.exit()

        elif m<=2 or m>=9 or n<0:
            print "Inavlid input. Enter an integer between 100 and 100,000,000.\n"

        else:
            L=[]

            for j in n:
                L.append(j)
                
            product_1 = 1
            for i in L:
                product_1 = product_1 * int(i)

            product_2=product_1
            for k in range (0,len(L)):
                product_2 = product_2/int(L[k])
                print product_2, 
                product_2 = product_1
            print "\n"
                

    except ZeroDivisionError:
        print "Invalid input. Entet a number without including 0.\n"
        print sys.exc_info()[0] , "\n"

    except ValueError:
        print "Invalid input. Enter a numerical integer values only.\n"
        print sys.exc_info()[0] , "\n"
        
    except :
        print "Error occured. Try again."
        print sys.exc_info()[0] , "\n"
