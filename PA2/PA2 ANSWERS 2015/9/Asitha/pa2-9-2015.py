def getText():
    try:
        fo=open("FileIn.txt","r")
        x=int(fo.read())
        fo.close()
        return x
    except IOError:
        print "File not found"
        pass
    except ValueError:
        print "Enter just an integers."
        pass
  
def showResult(x):
    if x==1 or x==2 or x==4 or x==8 or x==10:
        print "INVALID SCORE"
        return "INVALID SCORE"
        
    elif x%7==0:
        c_t=x/7
        t=0
        p=0
        
    elif x%7==1:
        c_t=x/7-1
        t=1
        p=1
        
    elif x%7==2:
        c_t=x/7-1
        t=0
        p=3
        
    elif x%7==3:
        c_t=x/7
        t=0
        p=1

    elif x%7==4:
        c_t=x/7-1
        t=1
        p=2

    elif x%7==5:
        c_t=x/7
        t=1
        p=0
        
    elif x%7==6:
        c_t=x/7
        t=0
        p=2

    answer=[]

    if c_t+t!=0:
        answer.append("Try: %s"%(c_t+t))
    if c_t!=0:
        answer.append("Conversion: %s"%(c_t))
    if p!=0:
        answer.append("Penalty/Drop Goals: %s"%(p))

    display="\n".join(answer)
    print display
    return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File Error"
        pass

try:    
    saveFile(showResult(getText()))
except:
    print "Something went wrong."
