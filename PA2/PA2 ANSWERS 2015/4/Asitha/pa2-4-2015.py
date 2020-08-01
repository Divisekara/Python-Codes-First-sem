def getText():
    try:
        fo=open("FileIn.txt","r")
        L=map(int,fo.read().split())
        fo.close()
        return L
    except IOError:
        print "File not found"
        pass
    except ValueError:
        print "Enter integers only"
        pass

def process(L):
    a=0
    for i in range(len(L)):        
        for j in range(len(L)):
            first=L[0:i]
            check=L[i:j+1][::-1]
            second=L[j+1:]
            n_L=first+check+second
            
            if n_L==sorted(L):
                s = "Yes " + " ".join(map(str,check))
                a=1
                break
        if a==1:
            break
    else:
        s = "No"
    print s
    return s  

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File error."
        pass

try:
    saveFile(process(getText()))
except:
    print "Something went wrong"
    pass
