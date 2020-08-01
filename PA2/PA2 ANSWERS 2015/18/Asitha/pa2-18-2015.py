def getText():
    try:
        fo=open("FileIn.txt","r")
        L=fo.read().split("\n")
        fo.close()
        for i in L:
            if not len(i)<20:
                print "Invalid Input. string out of range."
                break
        else:
            return L
    except IOError:
        print "File not found"
        pass
    
def int_float(x):
    try:
        if x.isdigit()==True:
            return "int"
        M=list(x)
        if M[0]=="+" or M[0]=="-":
            M.pop(0)
        a=0
        y="".join(M)
        if y.isdigit()==True:
            return "int"
        else:
            if ("." in y)==True:
                M.remove(".")
            z="".join(M)
            if z.isdigit()==True:
                return "float"
            else:
                return "no"
    except:
        return "no"

def date(x):
    try:
        M=list(x)
        if M.count("-")!=2:
            return "no"
        else:
            M.remove("-")
            M.remove("-")
            y="".join(M)
            if y.isdigit()==True:
                N=x.split("-")
                d=int(N[0])
                m=int(N[1])
                y=int(N[2])
                if 0<d<=31 and 0<m<=12 and 1991<y<=2999:
                    return "date"
                else:
                    return "no"
            else:
                return "no"
    except:
        return "no"

def show(L):
    answer=[]
    for i in L:
        if int_float(i)=="int":
            answer.append("int")
            continue
        elif int_float(i)=="float":
            answer.append("float")
            continue
        elif date(i)=="date":
            answer.append("date")
            continue
        else:
            answer.append("text")
            continue
    display="\n".join(answer)
    print display
    return display

def saveFile(s):
    fc=open("result.txt","w")
    fc.write(s)
    fc.close()

try:
    saveFile(show(getText()))
except:
    print "Something went wrong."
    pass
