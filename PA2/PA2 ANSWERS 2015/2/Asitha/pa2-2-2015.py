pivot=0
def getText():
    try:    
        fo=open("FileIn.txt","r")
        L=[]
        while True:
            L.append(fo.readline().split())
            if L[-1]==[]:
                L.pop(-1)
                break
        fo.close()
    except IOError:
        print "File not found"
        pass
    else:
        try:    
            i=int(L.pop(0)[0])
            M=map(int,L[0])
        except ValueError:
            print"Invalid input format"
            pass
        else:
            global pivot
            pivot=M.pop(i)
            return M

def show(M):
    less=[]
    greater=[]
    for j in M:
        if j<=pivot:
            less.append(j)
        else:
            greater.append(j)
    last=less+[pivot]+greater
    display=" ".join(map(str,last))
    print display
    return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File Error"
        pass
try:    
    saveFile(show(getText()))
except:
    print "Something went wrong"
