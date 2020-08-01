def getText(fname):
    try:
        fo=open(fname,'r')
        L=map(int,fo.read().split('\n'))
        fo.close()
        return L
    except IOError:
        pass
    except ValueError:
        pass

def M(n): #Male Function
    if n==0:
        return 0
    else:
        return n-F(M(n-1))
    
def F(n): #Female Function
    if n==0:
        return 1
    else:
        return n-M(F(n-1))

def process(L):
    lines=[]
    for i in L:
        line='%s: F=%s M=%s' %(str(i),str(F(i)),str(M(i)))
        lines.append(line)

    display='\n'.join(lines)
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
    s=raw_input()
    saveFile(process(getText(s)))
except:
    pass


