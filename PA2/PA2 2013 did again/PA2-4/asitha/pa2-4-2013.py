def getText():
    try:
        FileRead=open("FileIn.txt","r")
        L=list(FileRead.read())
        return L
    except IOError:
        print "File not found"
        pass

def converter(L):
    alpha=list("abcdefghijklmnopqrstuvwxyz")
    secret=[]
    for i in L:
        if (i in alpha)==True:
            n=alpha.index(i)
            secret.append(alpha[n-21])
        else:
            secret.append(i)
    return secret

def show(L):
    lines="".join(L)
    print lines
    return lines
    
def saveFile(string):
    try:
        FileCreate=open("reuslts.txt","w")
        FileCreate.write(string)
    except IOError:
        print "File Error"
        pass
    
try:
    saveFile(show(converter(getText())))
except:
    print "Somethin went wrong"
    pass
