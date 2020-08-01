def getText():
    try:
        FileOpen=open("FileIn.txt","r")
        L=FileOpen.read().split()
        FileOpen.close()
        if len(L)>=20:
            print "Invalid lenght of lines"
        else:
            for i in L:
                if len(i)>=50:
                    print "Invalid number of characters in a singlr line."
                    break
            else:
                return L
    except IOError:
        print "File Not found"
        

def palindrome(L):
    status=[]
    for i in L:
        a=0
        d=len(i)
        for j in range(d):
            for k in range(j+2,d):
                if i[j:k]==i[j:k][::-1] and (k-j)%2==0:
                    status.append("yes")
                    a=1
                    break
            if a==1:break
        else:
            status.append("no")
    return status

def show(L):
    line="\n".join(L)
    print line
    return line

def saveFile(s):
    try:
        FileCreate=open("result.txt","w")
        FileCreate.write(s)
        FileCreate.close()
    except IOError:
        print "File Error."
        pass

saveFile(show(palindrome(getText())))
        


    
