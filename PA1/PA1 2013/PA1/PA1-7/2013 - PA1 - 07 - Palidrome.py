#PA1 - 7 - Palindromes

print "Welcome to the palindrome Generator!"
a=1
while (a):
    try:
        n = raw_input("Enter an integer n where 1<=n<=80: ")
        m = int(n)
    except ValueError:
        print "Invalid Input! Enter numerical integer values only."
        continue
    else:
        if m==-1:
            print "Good Bye!"
            a=0
            continue
        elif m<1 or m>80:
            print "Invalid Input! Enter an interger between 0 and 81."
            continue
        else:
            b=1
            m=0
            while (b):
                num_list=[]
                rnum_list=[]
                for i in str(n):
                    num_list.append(i)
                num_list.reverse()
                rnum_list.extend(num_list)
                num_list.reverse()
                num = str("".join(num_list))
                rev_num = str("".join(rnum_list))
                if num==rev_num:
                    print "Palindrome = %d, Number of Additions = %d\n"%(int(num),m)
                    b=0
                    continue
                m+=1
                n=int(num)+int(rev_num)
                
                
