def getText():
    try:
        FileOpen=open("FileIn.txt","r")
        L=FileOpen.read().split()
        return L
    except IOError:
        print "file Not found"
        pass
    
def anagram(L):
    word1=list(L[0])
    word2=list(L[1])

    word1.sort()
    word2.sort()

    if word1==word2:
        return "Yes"
    else:
        return "No"
    
def show(s):
    print s
    return s

def saveFile(s):
    try:
        FileCreate=open("result.txt","w")
        FileCreate.write(s)
        FileCreate.close()
    except IOError:
        print "File Error"

try:
    saveFile(show(anagram(getText())))
except:
    print "Something went wrong."
    pass
