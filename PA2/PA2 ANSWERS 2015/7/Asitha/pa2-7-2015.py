def getText():
    try:
        fo=open("FileIn.txt","r")
        L=fo.read().split()
        fo.close()
        return L
    except IOError:
        print "File not found"
        pass

def substring(L):
    last=[]
    for x in L:
        answers=[]
        solution=[]
        i=x.lower()
        for j in range(len(i)):
            for k in range(j+1,len(i)+1):
                if j==k:
                    continue
                temp=i[j:k]
                real=list(set(temp))
                if len(real)==2:
                    answers.append(temp)
                    solution.append(x[j:k])
        lengths=[]
        for l in answers:
            lengths.append(len(l))
        if lengths.count(max(lengths))>1:
            for o in range(lengths.count(max(lengths))-1):
                lengths.remove(max(lengths))
                solution.pop(lengths.index(max(lengths)))
                
        y=lengths.index(max(lengths))
        last.append(solution[y])
    display="\n".join(last)
    print display
    return display
    
def saveFile(s):
    try:
        fc=open("reuslt.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File Error"
        pass
try:
    saveFile(substring(getText()))
except:
    print "Something went wrong."
