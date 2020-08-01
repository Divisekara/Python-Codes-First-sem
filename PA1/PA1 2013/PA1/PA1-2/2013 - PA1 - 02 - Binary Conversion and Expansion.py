#PA1 - 2 - Binary Conversion and Expansion

def decimal_to_binary(decimal):
    binary=""
    while decimal!=0:
        binary +=str(decimal%2)
        decimal/=2
    binary = binary[::-1]   
    return binary

'Here we define a function to perform the conversion, the built in function is "bin(decimal)"'

a=1
print "Welcome to the Decimal to Binary Converter and Expander!"
while (a):
    try:
        n = int(raw_input("Enter an integer n where 1<n<10,000: "))
    except ValueError:
        print "Invalid Input! Enter numerical integer values only."
        continue
    else:
        if n==0:
            print "Good Bye!"
            a=0
            continue
        elif n<0 or n>=10000:
            print "Invalid Input! Enter an interger between 0 and 10,000."
            continue
        else:
             m = decimal_to_binary(n)
             #b_list=[]
             #for i in bin(n):
                 #b_list.append(i)
             #b_list.remove("0")
             #b_list.remove("b")
             #m = "".join(b_list)
             exp=""
             for x in range(1,len(m)+1):
                 exp += "%s*2^%s"%(m[len(m)-x],x-1)
                 if x!=len(m):
                     exp+=" + "
             print "Output : %s = %s"%(m,exp)
             print"\n"
             
        
