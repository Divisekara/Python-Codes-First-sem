def getText():
    try:
        fo=open("FileIn.txt","r")
        L=[]
        while True:
            L.append(map(int,fo.readline().split()))
            if L[-1]==[]:
                L.pop(-1)
                break
        fo.close()
        return L
    except IOError:
        print "File not found."
        pass
        
def decrease(L):
    n_L=[]
    for i in L:
        if i>k:
            n_L.append(i//2)
            n_L.append(i-i//2)
        else:
            n_L.append(i)
    if max(n_L)>k:
        return decrease(n_L) #if there is no return except just decrease(n_L)
                             #there is no output given because it is not recursive    
    else:
        return n_L

def show(L):
    lines=[]
    for i in L:
        global k
        k=i[1]
        answer_list=decrease([i[0]])
        lines.append(len(answer_list))
        display="\n".join(map(str,lines))
    print display
    return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File error."
        pass

try:
    saveFile(show(getText()))
except:
    print "Something went wrong"
    pass
