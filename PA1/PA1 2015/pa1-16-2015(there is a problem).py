#### This code is not valid for all numbers
#### just for the decreasing one digit 



def decrease(x): #integer input  output integer type. with decreasde numbers
    L=[]
    num=list(str(x))
    for i in range(len(num)-1,-1,-1):
        num=list(str(x))
        num.pop(i)
        ans=int("".join(num))
        L.append(ans)
    return L


while True:
    try:    
        n=int(raw_input("Enter number: "))
    except ValueError:
        print "enter numerical positive integers only"
        continue
    else:
        if not 10<=n<10**100:
            print "enter numerical positive integers only greater than 10."
            continue
        if n%8==0:
            print "yes"

        else:
            while True:
                L=[]
                answer=0
                for i in decrease(n):
                    if i%8==0:
                        L.append(i)
                if len(L)>0:
                    answer=max(L)
                    break
                else:
                    break
                
            if answer!=0:
                print "yse m="+str(answer)

            else:
                print "No"
