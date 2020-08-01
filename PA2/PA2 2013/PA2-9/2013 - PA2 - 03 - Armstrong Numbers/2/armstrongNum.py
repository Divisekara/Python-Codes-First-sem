M=0
N=0
armNums=''
def getText():
    global M
    global N
    try:
        fr=open('FileIn.txt', 'r')
        M,N=tuple(fr.read().split())
        M,N=int(M),int(N)
        if N<=M:
            msg='M and N should be distinct such that N>M'
            print msg
            Msg(msg)
            return False
        elif M<0 or M>1000:
            msg='M out of range (0<M<1000)'
            print msg
            Msg(msg)
            return False
        fr.close()
        return True
    except IOError:
        msg='File not found or invalid file name/location'
        print msg
        Msg(msg)
        return False
    except ValueError:
        msg='Two integers must be input as M and N in the correct form'
        print msg
        Msg(msg)
        return False
    
def showArmstrongNumbers():
    global M
    global N
    global armNums
    output='M and N: '+str(M)+' '+str(N)+'\nArmstrong numbers between M and N: '+armNums
    print output
    Msg(output)
    return
def Msg(s):
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
    return
def isArmstrong(n):
    powerSum=0
    for dig in str(n):
        powerSum+=int(dig)**len(str(n))
    if n==powerSum:
        return True
    else:
        return False
if getText():
    armNumsList=[]
    for num in range(M,N+1):
        if isArmstrong(num):
            armNumsList.append(num)
    armNumsList=map(str,armNumsList)
    armNums=' '.join(armNumsList).strip()
    showArmstrongNumbers()        
    
    
    
