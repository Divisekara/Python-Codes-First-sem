#PA1 - 3 - ASCII Codes

print "Welcome to the ASCII Code Generator!"
a=1
while (a):
    try:
        n = raw_input("Enter an integer n where 999<n<10,000: ")
        m = int(n)
    except ValueError:
        print "Invalid Input! Enter numerical integer values only."
        continue
    else:
        if m<1000 or m>=10000:
            print "Invalid Input! Enter an interger between 999 and 10,000."
            continue
        else:
            for i in n:
                if i=="0":
                    print "Enter an integer which does not contain the digit 0"
                    break
                continue
            codes=""
            for i in n:
                codes+=chr(int(i)+96)
            codes+=" "
            p = n[0:2]
            if int(p)<=26:
                codes+=chr(int(p)+96)
                for t in range(2):
                    codes+=chr(int(n[t+2])+96)
                codes+=" "
            q = n[1:3]
            if int(q)<=26:
                codes+=chr(int(n[0])+96)
                codes+=chr(int(q)+96)
                codes+=chr(int(n[3])+96)
                codes+=" "
            r = n[2:4]
            if int(r)<=26:
                for t in range(2):
                    codes+=chr(int(n[t])+96)
                codes+=chr(int(r)+96)
                codes+=" "
            if int(p)<=26 and int(r)<=26:
                codes+=chr(int(p)+96)+chr(int(r)+96)
            print codes
            print "Number of Codes:",len(codes.split()),"\n"
        b = raw_input("Do you want to continue (y/n): ")
        if b=="n":
            a=0
                
                
