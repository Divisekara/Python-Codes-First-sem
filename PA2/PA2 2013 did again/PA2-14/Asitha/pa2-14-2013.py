N=0
def getText():
    try:    
        FileRead=open("FileIn.txt","r")
        L=[]
        while True:
            L.append(map(int,FileRead.readline().split()))
            if L[-1]==[]:
                break
        global N
        N=int(L.pop(0)[0])
        L.pop(-1)
        return L
    except ValueError:
        print "Non numerical data types represent as integers"
        pass
    except IOError:
        print "File Not Found"
        pass
    

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def calculate(L):
    answer=[]
    for i in L:
        a=gcd(i[0],i[1])
        b=gcd(a,i[2])
        answer.append(b)
    return answer

def show(numbers,answer):
    display=[]
    for i in range(N):
        line ="gcd (" + ",".join(map(str,numbers[i])) + ") = " + str(answer[i])
        display.append(line)
    lines = "\n".join(display)
    print lines
    return lines

def saveFile(s):
    try:
        FileCreate=open("result.txt","w")
        FileCreate.write(s)
        FileCreate.close()
    except IOError:
        print "File Error."
        pass

saveFile(show(getText(),calculate(getText())))
