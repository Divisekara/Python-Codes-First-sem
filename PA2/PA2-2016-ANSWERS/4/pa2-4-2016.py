N=0
M=0

def getText():
    try:
        fo=open("Input_1.txt","r")
        L=fo.read().split("\n")
        P=[]
        for i in L:
            P.append(map(int,i.split()))
        global N
        global M
        N=P.pop(0)[0]
        if not 1<=N<=100:
            print "out of range. Invalid Input"
        else: 
            return P[0:]
    except IOError:
        print "File not found."
        pass
    except ValueError:
        print "Enter integers only."
        pass

def show(L):
    answers=[]
    for i in L:
        
        M=i.pop(0)
        if not 1<=M<=100 or M!=len(i):
            break

        avg=float(sum(i))/M
        uppers=[]
        for j in i:
            if j>avg:
                uppers.append(j)
                
        percentage=round(float(len(uppers))/M*100,1)
        answers.append(percentage)
        
    display="\n".join(map(str,answers))
    print display
    return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File Error."
        pass
   
try:
    saveFile(show(getText()))
except:
    print "Something wrong."
