def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        if not 0<len(L)<=50:
            return 'Invalid number of lines'
        for i in L:
            if not 0<len(i)<=20:
                return 'Invalid length of a line'
        return L
    except IOError:
        pass
    
def change(L):
    answer=[]
    for i in L:
        chars=list(i)
        new=[]
        for j in chars:
            if j==' ':
                new.append(' ')
            else:
                n=ord(j)
                if n>=118:
                    n=n+5-26
                else:
                    n+=5
                new.append(chr(n))
        answer.append(''.join(new))
    return answer

def show(L):
    display='\n'.join(L)
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
    saveFile(show(change(getText())))
except:
    pass


    
