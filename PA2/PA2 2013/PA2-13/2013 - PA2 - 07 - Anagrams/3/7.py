global Output
Output = []

def getNum():
    Input=open("FileIn.txt","r")
    Str = Input.read()
    Numlist= Str.split( )
    if len(Numlist) == 2:
        M = Numlist[0]
        N = Numlist[1]
    else:
        print "Enter Only 2 words."
    global M,N
    Input.close
        
def Anagrome(M,N):
    List1 = list(M)
    List2 = list(N)
    List1.sort()
    List2.sort()

    if len(List1)!=len(List2):
            Output.append("No")
            
    else:
        for i in range(len(List1)):
            if List1[i]!=List2[i]:
                Output.append("No")
                break

def show():
    Anagrome(M,N)
    global Result
    if Output == []:
        Result = "Yes"
    else:
        Result = '\n'.join(Output)

    
def saveFile():
    Output=open("FileOut.txt","w")
    print Result
    Output.write(Result)
    Output.close

   
getNum()
show()

saveFile()
