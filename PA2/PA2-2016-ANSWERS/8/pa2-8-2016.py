n=0
def getText():
    try:
        fo=open("input_2.txt","r")
        L=fo.read().split("\n")
        global n
        n=int(L.pop(0))
        M=map(int,L)
        return M
    except IOError:
        print "File not found"
        pass
    except ValueError:
        print "Enter integers only."
        pass
    
def showResult(L):
    answers=[]
    for i in L:
        seq=[i]
        while i!=1:
            if i%2==0:
                i=i/2
            else:
                i=i*3+1
            seq.append(i)
        answers.append(len(seq))
    display="\n".join(map(str,answers))
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
    print "Something goes wrong."
    pass
