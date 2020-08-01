print "Welcome to the square difference program."
a=1
while (a):
    try:
        n=int(raw_input("Enter an integer between 0 and 100:"))
    except ValueError:
        print "Invalid Input. Enter numerical value integer only."
    else:
        if n==-1:
            print "Program terminated. Good Bye."
            break

        elif n<1 or n>=100:
            print "Invalid Input. Enter an integer between 1 and 100"
            continue

        else:   
            square=0
            sum_n=0
            for i in range(1,n+1):
                square+=i**2
                sum_n+=i
            print "answer:", sum_n**2-square

