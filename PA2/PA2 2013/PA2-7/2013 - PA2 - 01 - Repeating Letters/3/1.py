global List,Output
List = []
Output = []

def getNum():
    Input=open("FileIn.txt","r")
    i=0
    while i<31:
        Str = Input.readline()
        Str = Str.rstrip()
        if Str != '':
            List.append(Str)
            i += 1
        else:
            break
    Input.close
        
def Letters():
    for i in List:
        Let = list(i)
        Let.sort()
        Count = 0
        for i in range(len(Let)):
            if i != len(Let)-1:
                if Let[i]==Let[i+1]:
                    Count += 1
                    i += 1
                else:
                    continue
            else:
                break
       
        Output.append(Count)


def show():
    Showout = []
    for i in range(len(List)):
        Word1 = List[i]
        Number = Output[i]
        Join = "%s - %d" %(Word1,Number)
        Showout.append(Join)
    global Result
    Result = '\n'.join(Showout)
    
def saveFile():
    Output=open("FileOut.txt","w")
    print Result
    Output.write(Result)
    Output.close

   
getNum()
Letters()
show()
saveFile()

