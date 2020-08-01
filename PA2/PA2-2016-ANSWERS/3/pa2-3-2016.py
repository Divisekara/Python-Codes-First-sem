def getText():
    try:
        fo=open("FileIn.txt","r")
        L=fo.read().split("\n")
        fo.close()
        M=[]
        for i in L:
            M.append(map(int,i.split()))
        return M
    except IOError:
        print "File Not Found."
        pass
    except ValueError:
        print "enter integers only."
        pass

def show(L):
    answer=[]
    for i in L:
        n=i.pop(2)
        for j in range(n):
            i[i.index(max(i))]=max(i)/2
            if i.count(max(i))==2:
                i=[max(i),"SQUARE"]
                break 
        answer.append(" ".join(map(str,i)))
    display="\n".join(answer)    
    print display
    return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()    
    except IOError:
        print "File Error."
        pass

try:
    saveFile(show(getText()))
except:
    print "Something goes wrong."
    pass
