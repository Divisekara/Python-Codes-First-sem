def getNum():
    Input=open("FileIn.txt","r")
    Str = Input.read()
    global List
    List = Str.split('\n')
    Input.close


def showInitials():
    Namelist = []
    for i in List:
        Names = i.split()
        Initials = []
        for i in range(0,len(Names)-1):
            Letter = Names[i]
            Initials.append(Letter[0])
        Initials.append(Names[-1])
        Intname = '.'.join(Initials)
        Namelist.append(Intname)
    global Result
    Result = '\n'.join(Namelist)
    print Result

def saveFile():
    Output=open("FileOut.txt","w")
    Output.write(Result)
    Output.close

   
getNum()
showInitials()
saveFile()
