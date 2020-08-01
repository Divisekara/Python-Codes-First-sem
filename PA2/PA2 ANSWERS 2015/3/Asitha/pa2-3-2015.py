x=0
y=0

def getText():
    try:
        fo=open("FileIn.txt","r")
        L=map(int,fo.read().split())
        fo.close()
    except IOError:
        print "File not found"
        pass
    except ValueError:
        print "ebter integers only"
        pass
    else:
        global x
        global y
        x=L[0]
        y=L[1]
        if 1<=x<=6 and 1<=y<=6:
            pass
        else:
            print "invalid input. out of range number."
            pass

def process():
    L=[1,2,3,4,5,6]
    chance_x=[]
    chance_y=[]
    d=0
    for i in L:
        diff_x=abs(i-x)
        diff_y=abs(i-y)
        if diff_x==diff_y:
            d=1
        elif diff_x<diff_y:
            chance_x.append(i)
        else:
            chance_y.append(i)
    answer=" ".join(map(str,[len(chance_x),d,len(chance_y)]))
    print answer
    return answer

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File error."
        pass
    
try:        
    getText()
    saveFile(process())
except:
    print "something went wrong"
