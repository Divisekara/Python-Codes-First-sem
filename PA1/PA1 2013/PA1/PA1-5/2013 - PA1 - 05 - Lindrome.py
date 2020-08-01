#PA1 - 5 - Lindrome

print "Welcome to the Lindrome Evaluator!"
a=1
while (a):
    try:
        inp = str(raw_input("Enter Input: "))
    except TypeError:
        print "Invalid Input!"
        continue
    else:
        if inp=="0":
            print "Good Bye!"
            a=0
            continue
        else:
            L_half = []
            R_half = []
            if len(inp)%2==0:
                l_half = inp[:len(inp)/2]
                for i in l_half:
                    L_half.append(i)
                L_half.sort()
                r_half = inp[len(inp)/2:len(inp)]
                for i in r_half:
                    R_half.append(i)
                R_half.sort()
                if L_half==R_half:
                    print "YES","\n"
                else:
                    print "NO","\n"
            else:
                l_half = inp[:(len(inp)-1)/2]
                for i in l_half:
                    L_half.append(i)
                L_half.sort()
                r_half = inp[(len(inp)+1)/2:len(inp)]
                for i in r_half:
                    R_half.append(i)
                R_half.sort()
                if L_half==R_half:
                    print "YES","\n"
                else:
                    print "NO","\n"
