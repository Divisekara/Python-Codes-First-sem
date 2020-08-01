n=7
def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        global n
        n=int(L.pop(0))
        fo.close()
        return L[0].split()
    except IOError:
        pass

def show(L):
    answer=''
    for i in range(n):
        for j in range(n):
            word=L[j]
            try:
                answer+=word[i]
            except IndexError:
                pass
    print answer
    return answer

def saveFile(s):
    try:
        fo=open('result.txt','w')
        fo.write(s)
        fo.close()
    except IOError:
        pass
 
try:
    saveFile(show(getText()))
except:
    pass


    
