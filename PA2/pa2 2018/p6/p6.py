def getText(s):
    try:
        fo=open(s,'r')
        L=map(int,fo.read().split())
        fo.read()
        return L
    except IOError:
        pass
    except ValueError:
        pass
    
def process(L):
    answer=[]
    n=len(L)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if L[j]-L[i]==L[k]-L[j]:
                    answer.append('[%s, %s, %s][%s, %s, %s]'%(str(L[i]),str(L[j]),str(L[k]),i,j,k))
    return answer

def show(L):
    display='\n'.join(L)
    print display
    return display

def saveFile(s):
    try:
        fo=open('Output.txt','w')
        L=fo.write(s)
        fo.close()
    except IOError:
        pass

try:
    saveFile(show(process(getText(raw_input()))))
except:
    pass
