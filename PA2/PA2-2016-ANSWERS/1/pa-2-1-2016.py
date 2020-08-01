speed=0
length=0
distance=0

def getText():
    try:    
        fo=open("FileIn.txt","r")
        #fo=open("FileIn2.txt","r")
        L=map(int,fo.read().split("\n"))
        fo.close()
    except IOError:
        print "File not found"
        pass
    except ValueError:
        print "Invalid Input. Enter integers only."
        pass
    else:
        global speed
        global length
        global distance
        speed=L[0]
        length=L[1]
        distance=L[2]

def show():
    if 0<length<=6:
        if 85*5/18*2>distance:
            answer="DANGER\n%s"%(int(85.0*5/18*2))
        else:
            answer="SAFE"
        
    elif 6<length:
        extra=length-6
        if extra%3!=0:
            additional=(extra/3.0)+1
        else:
            additional=(extra/3)
        d=(additional+2)*speed/18.0*5
        if d>distance:
            answer="DANGER\n%s"%(d)
        else:
            answer="SAFE"
    else:
        print "Invalid length."
    print answer    
    return answer

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File Error."
        pass
 
try:
    getText()
    saveFile(show())
except:
    print "Something wrong."
    pass
