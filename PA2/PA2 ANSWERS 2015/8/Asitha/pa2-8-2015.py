base=0
def getText():
    try:
        fo=open("FileIn.txt","r")
        L=map(int,fo.read().split())
        fo.close()
    except IOError:
        print "File not found."
        pass
    except ValueError:
        print "enter integers only"
        pass
    else:
        number=L[0]
        global base
        base=L[1]
        return number

def converter(x):
    L=[]
    while x>0:
        if x%base==0:
            L.append(0)
        else:
            L.append(x%base)
        x=x/base
    converted_number=map(str,L)
    return converted_number

def show(L):
    term=[]
    for i in range(len(L)):
        term.append("%s*(%s**%s)"%(L[i],base,i))
    answer = "".join(L[::-1]) + " = " + " + ".join(term)
    print answer
    return answer

def saveFile(s):
    try: 
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File error."
        pass

saveFile(show(converter(getText())))
