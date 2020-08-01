#CA - 

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        words=fileOpen.read().plit()
        fileOpen.close()
    except IOError:
        print "File Error!"
    else:
        
        

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
    show(run)           
