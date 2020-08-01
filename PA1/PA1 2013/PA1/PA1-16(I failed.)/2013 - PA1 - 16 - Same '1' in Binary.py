#PA1 - 16 - Same "1" in Binary

def Dec_Bin(x):
    b_list = []
    while x!=0:
        b_list.append(x%2)
        x/=2
    b_list.reverse()
    return b_list

a = 1
while (a):
    try:
        X = int(raw_input("Input number X: "))
    except ValueError:
        print "Invalid Input!"
    else:
        x = Dec_Bin(X)
        y = x.count(1)
        i = 1
        while True:
            X2 = X+i
            u = Dec_Bin(X2)
            z = u.count(1)
            if z==y:
                break
            i+=1
        print "The answer:",X2,"\n"
        
