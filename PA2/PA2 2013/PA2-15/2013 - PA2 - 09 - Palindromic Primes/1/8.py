global List
List = []

def getNum():
    Input=open("FileIn.txt","r")
    Str = Input.read()
    Numlist= Str.split()
    if len(Numlist) == 1:
        N = int(Numlist[0])
    else:
        print "Enter Correct values for N."
    global N
    Input.close

        
def PalindromePrimes(N):
    Num = str(N)
    Rev = Num[-1::-1]
    if Num == Rev:
        for i in range(2,N+1):
            if i<N:
                if N%i==0:
                    i+=1
                    break
                else:
                    i+=1
            else:
                List.append(N)

def showPalindromePrimes(N):
    if len(List) < 6:
        for i in range(N,10000):
            PalindromePrimes(i)
            i+=1
    List2 = []
    for i in range(0,5):
        List2.append(str(List[i]))
    
    global Arm
    Arm = ' '.join(List2)

    
def saveFile():
    Output=open("FileOut.txt","w")
    Str = "Input N read from the file : %s\nFirst five PalindromePrimes > N : %s" %(N,Arm)
    print Str
    Output.write(Str)
    Output.close

   
getNum()
showPalindromePrimes(N)
saveFile()

