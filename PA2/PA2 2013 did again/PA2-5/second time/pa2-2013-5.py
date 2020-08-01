def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        if not 0<len(L)<50:
            return 'Invalid number of lines'
        return L
    except IOError:
        pass
    
def process(L):
    answers=[]
    for i in L:
        names=i.split()
        last_name=names.pop()
        initials=[]
        for j in names:
            if not 0<len(j)<20:
                return 'Invalid number of length per name'
            initials.append(j[0])
        initials.append(last_name)
        name_with_initials='.'.join(initials)
        answers.append(name_with_initials)
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
