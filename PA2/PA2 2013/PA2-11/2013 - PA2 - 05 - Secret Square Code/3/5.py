def getInp():
    Input=open("FileIn.txt","r")
    Str = Input.read()
    global List
    List = Str.split('\n')
    try:
        N= int(List[0])
    except TypeError:
        print "Enter Integer for the N value."
    else:
        List = List[1].split()
        global N

def show():
    NewList = []
    Output = []
    for i in range(0,N):
        NewList.append(['a']*N)
        List[i] = list(List[i])
    for i in List:
        if len(i)!= N:
            i.append('')
    
    for a in range(0,N):
        for b in range(0,N):
            NewList[a][b] = List[b][a]

    for i in NewList:
        Word = ''.join(i)
        Output.append(Word)
    global Result
    Result = ''.join(Output)

    
def saveFile():
    Output=open("FileOut.txt","w")
    print Result
    Output.write(Result)
    Output.close

   
getInp()
show()
saveFile()



