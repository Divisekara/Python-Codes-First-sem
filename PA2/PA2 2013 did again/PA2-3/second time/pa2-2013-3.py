def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        if not 0<len(L)<=50:
            return 'Invalid number of words'
        for i in L:
            if not 0<len(i)<=20:
                return 'Invalid length of input.'
        return L
    except IOError:
        pass

def checking(L):
    vowels=['a','e','i','o','u']
    answers=[]
    for i in L:
        v=[]
        for j in i:
            if (j in vowels)==True:
                v.append(j)
        if v.count(j)>1:
            continue
        M=sorted(v)
        if v==M and v!=[]:
            answers.append(i)
    return answers

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
    saveFile(show(checking(getText())))
except:
    pass
