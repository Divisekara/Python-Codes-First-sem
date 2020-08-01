def getText():
    try:
        fo=open("FileIn.txt","r")
        #fo=open("FileIn2.txt","r")
        L=map(int,fo.read().split())
        fo.close()
    except IOError:
        print "File not found."
        pass
    except ValueError:
        print "Enter integers only."
        pass
    else:
        for i in L:
            if i<0 or L.count(i)>1:
                print "Invalid input."
                break
        else:
            return L

def showResult(L):
    original=L[:]
    maxs=[]
    mins=[]
    for j in range(3):
        maxs.append(L.pop(L.index(max(L))))
        mins.append(L.pop(L.index(min(L))))

        n=original.index(maxs[j])
        m=original.index(mins[j])
        
        original.pop(n)
        original.insert(n,mins[j])
        
        original.pop(m)
        original.insert(m,maxs[j])

    display = " ".join(map(str,original))
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
    saveFile(showResult(getText()))
except:
    print "Something went wrong"
    pass 
