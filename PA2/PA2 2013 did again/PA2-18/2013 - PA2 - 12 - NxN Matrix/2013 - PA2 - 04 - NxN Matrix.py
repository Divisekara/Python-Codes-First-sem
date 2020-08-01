matA=[]
matB=[]
N=0
def getInput():
    global matA
    global N
    try:
        fr=open('FileIn.txt', 'r')
        N=int(fr.readline())
        line=0
        while line<N:
            row=fr.readline().split()
            if len(row)!=N:
                msg='Input matrix and the order should match'
                print msg
                Msg(msg)
                return False
            row=map(int, row)
            matA.append(row)
            line+=1
    except IOError:
        msg='File not found or invalid file name'
        print msg
        Mag(msg)
        return False
    except ValueError:
        msg='Please input integers as elements of matrix and single integer for order'
        print msg
        Msg(msg)
        return False
def show():
    for row in matB:
        row=map(str,row)
        print ' '.join(row).strip()
    return
def saveFile():
    display=''
    for row in matB:
        row=map(str,row)
        display+=' '.join(row).strip()+'\n'
    display.strip('\n')
    Msg(display)
    return
def Msg(s):
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
def calAvg():
    global matB
    for i in range(N):
        row=[]
        for j in range(N):
            eleSum=0
            n=0
            for l in range(-1,2):
                for m in range(-1,2):
                    try:
                        if (i==0 and l==-1) or (j==0 and m==-1):
                            continue
                        eleSum+=int(matA[i+l][j+m])
                        n+=1
                    except IndexError:
                        continue
            eleAvg=eleSum/n
            row.append(eleAvg)
        matB.append(row)
    return
if getInput():
    calAvg()
    show()
    saveFile()
