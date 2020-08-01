n=0
def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        global n
        n=int(L.pop(0))
        M=[]
        for i in L:
            M.append(map(int,i.split()))
        return M
    except IOError:
        pass
        
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def gcd2(a,b,c):
    return gcd(gcd(a,b),c)

def process(L):
    answers=[]
    for i in L:
        a=i.pop(0)
        b=i.pop(0)
        c=i.pop(0)
        answers.append(gcd2(a,b,c))
    return answers

def show(L,M):
    lines=[]
    for i in range(n):
        lines.append(('gcd (%s,%s,%s) = %s')%(str(M[i][0]),str(M[i][1]),str(M[i][2]),str(L[i])))
    display='\n'.join(lines)
    print display
    return display

def saveFile(s):
    try:
        fo=open('result.txt','w')
        fo.write(s)
        fo.close()
    except IOError:
        pass

try:
    saveFile(show(process(getText()),getText()))
except:
    pass

