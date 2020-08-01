alpha="abcdefghijklmnopqrstuvwxyz"

def getText():
    try:
        FileRead=open("FileIn.txt","r")
        L=list(FileRead.read())
        
    except IOError:
        print "File not found"
        pass
    
print getText()
