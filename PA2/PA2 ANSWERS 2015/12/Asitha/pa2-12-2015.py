def getText():
    try:
        fo=open("FileIn.txt","r")
        M=fo.read().split()
        fo.close()
    except IOError:
        print "File not found"
        pass
    else:
        L=[]
        for i in M:
            L.append(list(i))
        for j in L:
            if len(j)>256:
                print "Invalid number of lines."
                break
        else:
            return L
            
def showResult(L):
    lengths=[]
    for i in L:
        lengths.append(len(i))
    length=max(lengths)
    for j in L:
        space=length-len(j)
        j.extend([" "]*space)
    answer=[]
    for k in range(length):
        line=[]
        for j in range(len(L)):
            line.append(L[j][k])
        answer.append("".join(line))
    display="\n".join(answer)
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
    saveFile(showResult(getText()))
except:
    print "Something went wrong."
 
