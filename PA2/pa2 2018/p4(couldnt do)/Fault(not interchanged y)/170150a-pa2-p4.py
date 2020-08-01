def getText(s):
    try:
        fo=open(s,'r')
        L=fo.read().split('\n')
        return L
    except IOError:
        pass
    
def process(L):
    lists=[]
    for i in L:
        new_list=[]
        n=0
        m=0
        indexes=[]
        M=i.split()
        y=M.pop()
        x=M.pop()
        N=M[0].strip(']').strip('[').split(',')
        P=N[::]
        for j in N:
            n
            if j!=x and j!=y:
                z=P.index(j)
                new_list.append(P.pop(z))
            if j==x:
                m+=1
                indexes.append(n)
            n+=1
        for k in range(m):
            new_list.insert(indexes[k],x)
            new_list.insert(indexes[k]+1,y)

        lists.append(str(map(int,new_list)))
    return lists

def show(L):
    display='\n'.join(L)
    print display
    return display

def saveFile(s):
    try:
        fo=open('Output.txt','w')
        fo.write(s)
        fo.close()
    except:
        pass
try:
    s=raw_input()
    saveFile(show(process(getText(s))))
except:
    pass
