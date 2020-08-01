n=int(raw_input("Enetr number:"))
x=len(str(n))*" "
print x

while n>1:
    if n%3==0:
        print n,"- 0"
        n=n/3
    elif (n+1)%3==0:
        print n,"- 1"
        n=(n+1)/3
    elif (n-1)%3==0:
        print n,"- -1"
        n=(n-1)/3
print n
