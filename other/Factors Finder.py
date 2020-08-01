while True:
    n=int(input("Give a number that you want to find the factors-: "))
    x=1
    while x<=n:
        if n%x==0:
            print x, " is a factor."
        x=x+1

    
