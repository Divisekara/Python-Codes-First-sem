m=0
n=0

def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split()
        fo.close()
        global n
        global m
        n=int(L.pop(0))
        m=int(L.pop(0))
    except IOError:
        pass

def process():
    answers=[]
    for i in range(n,m):
        digits=list(str(i))
        calculated=0
        exp=len(digits)
        for j in digits:
            calculated+=int(j)**exp
        if i==calculated:
            answers.append(i)
    return answers

def show(L):
    display='M and N: %s %s \n'%(n,m)
    display+='Armstrong numbers between M and N: ' + ' '.join(map(str,L))
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
    getText()
    saveFile(show(process()))
except:
    pass
