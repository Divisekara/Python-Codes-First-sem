n=0
def getText():
    try:
        fo=open("FileIn.txt","r")
        L=map(int,list(fo.read()))
        fo.close()
    except IOError:
        print "File not found."
        pass
    except ValueError:
        print "Enter integers only."
        pass
    else:
        global n
        n=len(L)
        if not 1<=len(str(n))<=100:
            print "Invalid input"
        else:
            return L

def showResult(L):
    answer=[]
    for i in range(n+1):
        for j in range(i+1,n+1):
            temp=L[i:j]
            number=int("".join(map(str,temp)))
            product=1
            for l in temp:
                product*=l
            if number==sum(temp)*product:
                x=int("".join(map(str,temp)))
                if not x in answer:
                    answer.append(x)
    if answer==[]:
        print "none"
        return "none"
    else:
        display = " ".join(map(str,answer))
        print display
        return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File error."
        pass
    
try:
    saveFile(showResult(getText()))
except:
    print "Something went wrong."
    pass
