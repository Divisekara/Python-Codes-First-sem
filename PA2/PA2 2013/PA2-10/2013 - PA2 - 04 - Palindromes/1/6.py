global Output
Output = []

def getInp():
    Input=open("FileIn.txt","r")
    Str = Input.read()
    global List
    List = Str.split('\n')
    print List   
        
def EvenPalindrome():
    for i in List:
        Letters = list(i)
        for j in range(len(Letters)):
            if j != (len(Letters)-1):
                if Letters[j] == Letters[j+1]:
                    Output.append("Yes")
                    break
            else:
                Output.append("No")
            
    global Result
    Result = '\n'.join(Output)

    
def saveFile():
    Output=open("FileOut.txt","w")
    print Result
    Output.write(Result)
    Output.close

   
getInp()
EvenPalindrome()
saveFile()




