global List
List = []

def getNum():
    Input=open("FileIn.txt","r")
    Str = Input.read()
    Numlist= Str.split()
    if len(Numlist) == 2:
        M = int(Numlist[0])
        N = int(Numlist[1])
    else:
        print "Enter Correct values for M and N."
    global M,N
    Input.close

def Armstrong(N):
    Numlist = list(N)
    Power = len(Numlist)
    Total = 0
    for i in Numlist:
        Total += int(i)**Power
    if Total == int(N):
        List.append(N)
        
def showArmstrogNumbers():
    for i in range(M,N+1):
        NumStr = str(i)
        Armstrong(NumStr)
        global Arm
        Arm = ' '.join(List)

def saveFile():
    Output=open("FileOut.txt","w")
    Str = "M and N : %d %d \nArmstrong Numbers Between M and N : %s" %(M,N,Arm)
    print Str
    Output.write(Str)
    Output.close

   
getNum()
showArmstrogNumbers()
saveFile()
