def getText():
    try:        
        FileOpen=open("FileIn.txt","r")
        L=[]
        while True:
            L.append(FileOpen.readline().split())
            if L[-1]==[]:
                break
        FileOpen.close()
    except IOError:
        print "File Not Found"
    else:
        L.pop(-1)
        return L

def calculations(L):
    L1=[]
    for i in L:
        Temp=[]
        Temp.append(i.pop(0))
        Temp.append(sum(map(int,i)))
        Temp.append(round(float(sum(map(int,i)))/len(i),2))
        L1.append(Temp)
    sums=[]
    for j in L1:
        sums.append(j[1])   
    ranks=sorted(sums)[::-1]
    for k in L1:
        k.append(ranks.index(k[1])+1)     
    return L1
    
def show(L):
    L1=[]
    for i in L:
        L1.append(" ".join(map(str,i)))
    lines="\n".join(L1)
    print lines
    return lines

def saveFile(s):
    try:
        FileCreate=open("result.txt","w")
        FileCreate.write(s)
        FileCreate.close()
    except IOError:
        print "File Error"
        pass

    
        
    
saveFile(show(calculations(getText())))
