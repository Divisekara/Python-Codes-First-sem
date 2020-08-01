def getInp():
    Input=open("FileIn.txt","r")
    Str = Input.read()
    List = Str.split('\n')
    try:
        N= int(List[0])
    except TypeError:
        print "Enter Integer for the N value."
    else:
        global Letters
        Letters = list(List[1])
        print Letters
        global N

def show():
    Output = []
    while len(Letters)>0:
        print len(Letters)
        for i in range(0,len(Letters)):
            if Letters[i] == ' ':
                Output.append(Letters[i+1])
                Letters.pop(i+1)
            else:
                continue
    print Output
##    for i in NewList:
##        Word = ''.join(i)
##        Output.append(Word)
##    global Result
##    Result = ''.join(Output)

    
def saveFile():
    Output=open("FileOut.txt","w")
    print Result
    Output.write(Result)
    Output.close

   
getInp()
show()
##saveFile()



