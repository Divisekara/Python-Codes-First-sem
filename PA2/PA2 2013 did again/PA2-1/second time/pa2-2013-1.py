n=0
m=0

def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()
        x=L.pop(0).split()
        global n
        global m
        n=int(x.pop(0))
        m=int(x.pop(0))
        return L
    except IOError:
        pass
    except ValueError:
        pass
    
def calculate(L):
    names=[]
    avgs=[]
    total=0
    for i in L:
        datum=i.split()
        names.append(datum.pop(0))
        
        sum_=sum(map(int,datum))
        avgs.append(float(sum_)/m)
        total+=sum_
    avgs.insert(0,float(total)/(n*m))
    names.insert(0,'Class')

    return names,avgs

def show(names,avgs):
    L=[]
    for i in range(n+1):
        L.append('%s average: %.2f' %(names[i],avgs[i]))
    display='\n'.join(L)
    print display
    return display

def saveFile(display):
    try:
        fo=open('result.txt','w')
        fo.write(display)
        fo.close()
    except IOError:
        pass
try:
    saveFile(show(calculate(getText())[0],calculate(getText())[1]))
except:
    print 'something goes wrong'
    pass
            

