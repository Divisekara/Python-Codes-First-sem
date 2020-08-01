E=0
def getText():
    try:
        fo=open("FileIn.txt","r")
        L=fo.read().split()
        fo.close()
    except IOError:
        print "File not found"
        pass
    else:
        global E
        E=int(L.pop(0))
        if not E<1000:
            print "Invalid input. Out of range."
            pass
        else:
            return L

def showResults(L):
    answer=[]
    for i in range(len(L[0])):
        for j in range(E):
            try:
                answer.append(L[j][i])
            except IndexError:
                pass
    display = "".join(answer)
    print display
    return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print ""

#try:
saveFile(showResults(getText()))

"""
except ValueError:
    print "Something went wrong."
    pass
"""
