n=2520

while True:
    for i in range(1,21):
        if n%i!=0:
            break
    else:
        print n
        break
    n=n+2520
