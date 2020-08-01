def integer(x):
    try:
        if x.isdigit()==True:
            return True
        L=list(x)
        a=L.pop(0)
        num=''.join(L)
        if (a=='+' or a=='-') and num.isdigit()==True:
            return True
        elif a.isdigit()==False:
            return False
        else:
            if num.isdigit()==True:
                return True
            else:
                return False
    except:
        return False

def floating(x):
    try:
        L=list(x)
        if ('.' in L)==True:
            L.remove('.')
            a=L.pop(0)
            num=''.join(L)
            if (a=='+' or a=='-') and num.isdigit()==True:
                return True
            elif a.isdigit()==False:
                return False
            else:
                if num.isdigit()==True:
                    return True
                else:
                    return False
        else:
            return False
    except:
        return False
    
	
def date(x):
    try:
        L=list(x)
        if L[2]!='-' or L[5]!='-' or L.count('-')!=2 or len(L)!=10:
            return False
        else:
            L.remove('-')
            L.remove('-')
            d=int(''.join(L[:2]))
            m=int(''.join(L[2:4]))
            y=int(''.join(L[4:]))
            
            if 0<d<=31 and 0<m<=12 and y>0:
                return True
            else:
                return False
    except:
        return False
    

def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        return L
    except IOError:
        pass
    
def checking(L):
    answer=[]
    for i in L:
        if integer(i)==True:
            answer.append('Integer')
            continue
        elif floating(i)==True:
            answer.append('Float')
            continue
        elif date(i)==True:
            answer.append('Date')
            continue
        else:
            answer.append('String')

    return answer

def show(L):
    display='\n'.join(L)
    print display
    return display

def saveFile(s):
    try:
        fo=open('result.txt','w')
        fo.write(s)
        fo.close()
    except IOError:
        pass
try:
    saveFile(show(checking(getText())))
except:
    pass

        
    
        
    
    
