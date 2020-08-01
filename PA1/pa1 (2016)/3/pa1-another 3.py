while True:
    try:
        L=map(int,raw_input("Enter number list: ").split())
    except ValueError:
        print "Invalid input.. ENTER INTEGRS ONLY."
        continue
    else:
        order=[]

        n=1
        for i in L:
            if L.count(i)>1:
                order.append(n)
            n += 1
        if len(order)==0:
            print None
        else:
            print " ".join(map(str,order))
    finally:
        print ""


"""

1 3 5 7 8 90 7 56 33 90 -1

1 3 5 7 90 56 33 91 -1

5 5 5 5 1 5 5 -1

"""
