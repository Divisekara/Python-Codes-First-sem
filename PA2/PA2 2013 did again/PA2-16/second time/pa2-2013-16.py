def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        return L
    except IOError:
        pass

def process(L):
    lines=[]
    for i in L:
        chars=list(set(list(i)))
        lines.append('%s - %s'%(i,len(chars)))
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
    saveFile(process(getText()))
except:
    pass
