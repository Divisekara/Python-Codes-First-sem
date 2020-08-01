def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        return L
    except IOError:
        pass

def process(L):
    answer=[]
    for i in L:
        n=0
        letters=list(i)
        set_letters=list(set(letters))
        for j in set_letters:
            if letters.count(j)>1:
                n+=1
        answer.append(n)
    return answer

def show(L,M):
    lines=[]
    for i in range(len(L)):
        lines.append(str(L[i]) + ' - ' + str(M[i]))
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
    saveFile(show(getText(),process(getText())))
except IOError:
    pass
