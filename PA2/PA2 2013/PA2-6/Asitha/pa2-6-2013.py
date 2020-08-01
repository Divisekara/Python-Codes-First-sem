def getText():
    try:    
        FileOpen=open("FileIn.txt","r")
        L=FileOpen.read().split()
        return L
    except IOError:
        print "File is not found"
        pass

def permuterns(L):
    solutions=[]
    for i in L:
        perms=[]
        for j in range(len(i)):
            last=i[0:j]
            first=i[j:]
            word=first+"$"+last
            perms.append(word)
        solutions.append(" ".join(perms))
    return solutions

def show(L):
    lines="\n".join(L)
    print lines
    return lines

def saveFile(L):
    try:
        FileCreate=open("result.txt","w")
        FileCreate.write(L)
    except:
        print "File Error."
        pass
try:
    saveFile(show(permuterns(getText())))
except:
    print "Something went wrong"
    pass


