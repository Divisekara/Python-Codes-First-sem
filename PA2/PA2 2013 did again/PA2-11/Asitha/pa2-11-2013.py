n=0
words=[]
def getText():
    try:
        FileOpen=open("FileIn.txt","r")
        L=map(list,FileOpen.read().split())
        FileOpen.close()
    except IOError:
        print "File Not Found"
        pass
    else:
        global n
        global words
        n=map(int,L[0])[0]
        print n
        words=L[1:]

def convert():
    line=""
    for i in range(n):
        for j in words:
            try:
                line += j[i]
            except IndexError:
                continue
    return line

def show(s):
    print s

def saveFile(s):
    try:    
        FileCreate=open("result.txt","w")
        FileCreate.write(s)
        FileCreate.close()
    except IOError:
        print "File error."
        pass
    
getText()
show(convert())
saveFile(convert())
