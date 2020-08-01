def getText():
    try:        
        FileOpen=open("FileIn.txt","r")
        L=map(int,FileOpen.read().split())

    except IOError:
        print "File Not found"
        pass
    except ValueError:
        print "Enter numerical integers only."
        pass
    
    else:
        M=L[0]
        N=L[1]
        if not 0<M<1000 or not M<N<10000:
            print "Invalid Input"
            pass
        
        else:
            return M,N
     
def compute(M,N):
    #M N are integers and output the Armstrong Numbers
    solutions=[]
    for i in range(M,N):
        L=list(str(i))
        n=len(L)
        sum_=0
        for j in L:
            sum_ += (int(j))**n
        if sum_ == i:
            solutions.append(i)
    return solutions

def show(L):
    #Displaying a list in a line
    line ="Armastrong numbers between M and N: " + " ".join(map(str,L))
    print line
    return line

def saveFile(s):
    try:        
        FileCreate=open("result.txt","w")
        FileCreate.write(s)
        FileCreate.close()
    except IOError:
        print "File error."

saveFile(show(compute(getText()[0],getText()[1])))



