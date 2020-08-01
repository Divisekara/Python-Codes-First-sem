M=0
N=0

def getText():
    try:    
        fo=open("FileIn.txt","r")
        L=[]
        while True:
            L.append(fo.readline().split())
            if L[-1]==[]:
                L.pop(-1)
                break
        fo.close()
    except IOError:
        print "File Not Found"
        pass
    else:
        try:
            global M
            global N
            M = int(L[0][0])
            N = int(L[0][1])
        except ValueError:
            print "Invalid format included in text"
            pass
        else:
            L.pop(0)
            if not N==len(L):
                print "Wrong number of data"
                    
            else:
                return L

def show(L):
    mass=[]
    for i in L:
        mass.append((float(i[1])**3)*float(i[2]))
    answer=L[mass.index(max(mass))][0]
    print answer
    return answer

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "file error."
        pass
try:
    saveFile(show(getText()))
except IndexError:
    print "Invalid input."
    pass
except:
    print "something went wrong"
    pass
