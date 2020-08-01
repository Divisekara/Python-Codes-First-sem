while True:
    try:
        seq=map(int,raw_input("Enter sequence: ").split())
    except ValueError:
        print "enter integers only"
        continue
    else:
        if len(seq)<2:
            print "enter squence having more than one term"
            print "not nice"
            continue
        for i in range(1,len(seq)):
            if i%2==0:
                if seq[i-1]>seq[i]:
                    continue
                else:
                    print "not nice"
                    break
                
            else:
                if seq[i-1]<seq[i]:
                    continue
                else:
                    print "not nice"
                    break
        else:
            print "nice"



"""
2 5 1 100 99 120
nice

2 5 3 2
not nice
"""
