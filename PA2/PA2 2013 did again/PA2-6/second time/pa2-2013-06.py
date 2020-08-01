def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        if not 0<len(L)<50:
            return 'Invalid number of words.'
        for i in L:
            if not 0<len(i)<20:
                return 'Invalid number of length'
        return L
    except IOError:
        pass

def process(L):
    answers=[]
    for i in L:
        words=[]
        for j in range(len(i)):
            words.append(i[j:]+'$'+i[:j])
        answers.append(' '.join(words))
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
    saveFile(show(process(getText())))
except:
    pass
