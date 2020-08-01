def getText():
    try:
        file_Object=open("FileIn.txt","r")
        L=file_Object.read().split()
        if not 0<len(L)<50:
            pass
        for i in L:
            if i.islower()==False:
                print "There are uppercase letters input words."
                break
        else:
            return L
    except IOError:
        print "File Not found"

def vowel_check(L):
    words=[]
    for i in L:
        letters=[]
        a=0
        b=0
        for j in i:
            if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
                letters.append(j)
                b=1
                if letters.count(j)!=1:
                    a=1
        if letters!=sorted(letters):
            a=1
        if a==1:
            continue
        elif b==1:
            words.append(i)
    return words


def show(words):
    for i in words:
        print i


def saveFile(words):
    try:        
        fileCreate=open("result.txt","w")
        for i in words:
            fileCreate.write(i)
            fileCreate.write("\n")
    except IOError:
        print "File  Error"
        pass
try:
    L=getText()
    words=vowel_check(L)
    show(words)
    saveFile(words)
except:
    print "Something went wrong."
    pass
    

