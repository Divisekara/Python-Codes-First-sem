def five_check(L):
    u=0
    d=0
    for i in range(0,4):
        diff=L[i]-L[i+1]
        if diff<0:
            u+=1
        elif diff>0:
            d+=1
    if u==4:
        return "upward"
    elif d==4:
        return "downward"
    else:
        return "unpredictable"


while True:
    try:
        L=map(int,raw_input().split())
    except ValueError:
        print "enter numerical integers only\n"
    else:
        status=[]
        for i in range(len(L)-4):
            status.append(five_check(L[i:i+5]))
        print "Trend:" , ", ".join(status) , "\n"
    

