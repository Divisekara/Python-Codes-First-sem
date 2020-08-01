def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split('\n')
        fo.close()    
        return L
    except IOError:
        pass
    
def process(L):
    answer=[]
    for i in L:
        status=''
        n=len(i)
        for j in range(n):
            for k in range(j+2,n):
                temp=i[j:k]
                if temp==temp[::-1]:
                    status='yes'
                    break
            if status=='yes':
                answer.append(status)
                break
        else:
            status='no'
            answer.append(status)
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
    saveFile(show(process(getText())))
except:
    pass
