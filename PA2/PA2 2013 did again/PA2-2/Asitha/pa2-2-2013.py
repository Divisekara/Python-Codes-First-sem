def getText():
    try:
        fileOpen=open("FileIn.txt","r")
        L=fileOpen.read().split()
        fileOpen.close()
    except IOError:print "Invalid Input"
    else:
        if len(L)<50:
            for i in L:
                if len(i)<=20:
                    continue
                else:
                    print "Invalid Input"
                    break
            else:return L
        else:print "Invalid Input"

def Date(x):
    chars=list(x)
    if len(chars)==10 and chars[2]=='-' and chars[5]=='-':
        try:
            if int("".join(chars[0:2]))<=31 and int("".join(chars[3:5]))<=12:
                a=int("".join(chars[6:]))
                return 1
        except ValueError:
            return 0
    else:
        return 0

def Int(x):
    chars=list(x)
    try:
        a=int("".join(chars))
    except ValueError:
        return 0
    else:
        return 1

def Float(x):
    chars=list(x)
    for i in chars:
        if i==".":
            try:
                a=float("".join(chars))
            except ValueError:
                return 0
            else:
                return 1
    else:
        return 0
            
def Show(L):
    output=[]
    for i in L:
        if Int(i)==1:
            output.append("int")
            continue
        elif Float(i)==1:
            output.append("float")
            continue
        elif Date(i)==1:
            output.append("date")
            continue
        else:
            output.append("text")
            continue
        
    display=''
    for j in output:
        display+=j+"\n"
        
    return display
    
print Show(getText())

def SaveFile(x):
    try:
        fileWrite=open("result.txt","w")
        fileWrite.write(x)
        fileWrite.close()
    except IOError:
        print "File error."
        
SaveFile(Show(getText()))
