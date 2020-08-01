#PA1-24 - Digit Triangle

print "Welcome to the Digit Triangle Generator!"
a=1
while (a):
    try:
        n = int(raw_input("Enter an integer n: 0<n<50 (The height of the triangle): "))
    except ValueError:
        print "Invalid input! Input should be an numeric integer value between 0 and 50."
        continue
    else:
        if n==-1:
            print "Good Bye!"
            a=0
            continue
        elif n<=0 or n>=50:
            print "Invalid Input! Input should be an integer inbetween 0 and 50."
            continue
        else:
            line = ""
            triangle = ""
            for x in range(1,n+1):
                for z in range(n-x):
                    line+=" "*4
                for y in range(-x,x+1):
                    if y==-1 or y==0:
                        continue
                    else:
                        line+=str("%4d"%(abs(y))) #str(format(abs(y),"4d"))
                triangle+=line+"\n"
                line=""
            print triangle
                
