N=0
def getText():
    try:
        fo=open("FileIn.txt","r")
        #fo=open("FileIn2.txt","r")
        L=fo.read().split("\n")
        fo.close()
    except IOError:
        print "File not found"
        pass
    else:
        try:
            if not 1<=len(L)<=100:
                print "Invalid input. Sequence out of range."
                pass
            else:
                global N
                N=int(L.pop(-1))
                M=map(int,L[0].split())
                return M
        except ValueError:
            print "Enter integers only"
            pass

def show(L):
    try:
        n=0
        while n!=N:
            n_L=[]
            for i in range(len(L)-1):
                n_L.append(L[i+1]-L[i])
            L=n_L[:]    
            n+=1

        display = " ".join(map(str,L))
        print display
        return display
    except IndexError:
        print "Invalid Input."
        pass
    
def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File Error"
        pass

saveFile(show(getText()))
