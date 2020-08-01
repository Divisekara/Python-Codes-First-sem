def getText():
    try:
        fo=open("FileIn.txt","r")
        L=fo.read().split()
        fo.close()
        
    except IOError:
        print "File not found"
        pass
    else:
        if len(L)<1000:
            for i in L:
                if len(i)<20 and i.isalpha()==True:
                    continue
                else:
                    print "Invalid nput"
                    break
            else:
                return L
        else:
            print "Invalid input."
    
def showResult(L):
    answer=[]
    for i in L:
        word=list(i.lower())
        sorted_word=sorted(word)
        if word==sorted_word:
            answer.append(i)
    display=" ".join(answer)
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
    print "Something went wrong"
    pass
