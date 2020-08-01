x=0
def getText():
    try:
        fo=open("FileIn.txt","r")
        global x
        x=int(fo.read())
        fo.close()
    except IOError:
        print "File not found."
        pass
    except ValueError:
        print "Invalid input. enter integers only."
        pass

def showResults():
    global x
    b_number=list(bin(x)[2:])
    ones_1=b_number.count("1")
    while True:
        x+=1
        ones_2=list(bin(x)[2:]).count("1")
        if ones_1==ones_2:
            print x
            return x

def saveFile():
    try:
        fc=open("result.txt","w")
        fc.write(str(x))
        fc.close()
    except IOError:
        print "File error."
        pass

try:
    getText()
    showResults()
    saveFile()
except:
    print "Something went wrong"
    pass
