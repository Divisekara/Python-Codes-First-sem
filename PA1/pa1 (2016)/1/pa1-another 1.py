while True:
    try:
        x=map(int,raw_input("Enter two numbers N and k: ").split())
    except ValueError:
        print "Invalid input. Enter positive integers only."
    else:
        if len(x)!=2:
            print "Invalid number of parameters"
            continue
            
        N=x[0]
        K=x[1]
        pair=0

        for i in range(N+1):
            for j in range(i+1,N+1):
                if i+j==K:
                    pair +=1

        print pair

    finally:
        print ""            











