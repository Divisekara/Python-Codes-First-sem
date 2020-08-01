def getText(s):
    try:
        fo=open(s,'r')
        L=map(int,fo.read().split('\n'))
        fo.close()
        return L
    except IOError:
        pass
    except ValueError:
        pass

def process(L):
    answer=[]
    for i in L:
        n=2
        M=[]
        while i!=1:
            if i%n==0:
                i=i/n
                M.append(n)
            else:
                n+=1
        x=', '.join(map(str,M))
        answer.append('['+x+']')
    return answer

def show(L):
    display='\n'.join(map(str,L))
    print display
    return display

def saveFile(s):
    try:
        fo=open('Output.txt','w')
        fo.write(s)
        fo.close()
    except IOError:
        pass

try:
    saveFile(show(process(getText(raw_input()))))
except:
    pass
