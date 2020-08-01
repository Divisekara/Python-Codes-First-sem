#CA - 02 - Type of Each String

def getText():
#To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        List=fileOpen.read().split("\n")
        fileOpen.close()
    except IOError:
        print "File Error!"
    else:
        if len(List)<50:
            for i in List:
                if len(i)<20:
                    continue
                else:
                    print "Invalid Input!"
                    break
            else:
                return List
        else:
            print "Invalid Input!"
        
def Date(N):
    Letters = list(N)
    if len(Letters) == 10:
        if Letters[2] == '-' and Letters[5] == '-':
            if int("".join(Letters[0:2]))<=31 and int("".join(Letters[3:5]))<=12:
                Letters.remove("-")
                Letters.remove("-")
                Date = ''.join(Letters)
                try:
                    int(Date)
                except ValueError:
                    return 0
                else:
                    return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def Int(N):
    try:
        int(N)
    except ValueError:
        return 0 
    else:
        return 1
        
def Float(N):
    Letters = list(N)
    for i in Letters:
        if i == '.':
            Num = ''.join(Letters)
            try:
                float(Num)
            except ValueError:
                return 0  
            else:
                return 1
    else:
        return 0       

def show(List):
    #To print the output on screen as well as write to a file.
    Output = []
    for i in List:
        if Date(i)==0:
            if Float(i)==0:
                if Int(i)==0:
                    Output.append("text")
                else:
                    Output.append("int")
            else:
                Output.append("float")
        else:
            Output.append("date")
    output = "\n".join(Output)
    print output
    try:
        fileWrite=open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()   #To call functions in a global level                                                                                  
if run!=None:
    show(run)
