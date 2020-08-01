#CA - 05 - Initials with the last Name

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
def showInitials(x):
    Namelist = []
    for i in x:
        Names = i.split()
        Initials = []
        for i in range(0,len(Names)-1):
            Letter = Names[i]
            Initials.append(Letter[0])
        Initials.append(Names[-1])
        Intname = '.'.join(Initials)
        Namelist.append(Intname)
    output = '\n'.join(Namelist)
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
    show(showInitials(run)) 


