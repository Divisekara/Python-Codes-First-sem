#CA - 04 - Secret Codes

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        words=fileOpen.read().split("\n")
        fileOpen.close()
    except IOError:
        print "File Error!"
    else:
        return words
   
def code(x): 
    output = ""
    for i in x:
        Output = []
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
        Line = " ".join(Words)
        Output.append(Line)
        output += " ".join(Output)+"\n"
    return output

def show(output):
    #To print the output on screen as well as write to a file.
    print output
    try:
        fileWrite=open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()   #To call functions in a global level                                                                                  
if run!=None:
    show(code(run))  
