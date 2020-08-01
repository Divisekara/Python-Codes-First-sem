def getInp():
    Input=open("FileIn.txt","r")
    Str = Input.read()
    global List
    List = Str.split('\n')
   
def show():    
    Output = []
    for i in List:
        Words = i.split()
        for j in range(len(Words)):
            Letters = list(Words[j])
            for k in range(0,len(Letters)):
                Num = ord(Letters[k]) + 5
                if Num > 123:
                    NewLet = chr(Num-97)
                else:
                    NewLet = chr(Num)
                Letters[k] = NewLet
            NewWord = ''.join(Letters)
            Words[j] = NewWord
        Line = ' '.join(Words)
        Output.append(Line)            
    global Result
    Result = '\n'.join(Output)
  
def saveFile():
    Output=open("FileOut.txt","w")
    print Result
    Output.write(Result)
    Output.close

   
getInp()
show()
saveFile()



