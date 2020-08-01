while True:
    try:
        L=list(map(int,raw_input("Enter the heights: ").split()))

    except ValueError:
        print "Enter numerical Integers only"
        continue

    else:
        for k in L:
            if not 100<=k<=200:
                print "Impossible height.",k
                continue
        if not 100<=k<=200:continue
        
        pair=0
        n=0
        while True:
            try:
                term=L[n]
            except IndexError:
                break
            else:
                num=L.count(term)
                if num>=2:
                    pair += num/2
                    for j in range(num):
                        L.remove(term)
                else:
                    n += 1
        print pair
        
    finally:
        print ""
                

"""
135 130 135 150 140 135
135 130 145 135 140 145 150 155
135 130 135 135 140 135 135
"""
