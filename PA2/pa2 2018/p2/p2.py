def getText(s):
    try:
        fo=open(s,'r')
        L=fo.read().split('\n')
        fo.close()
        return L
    except IOError:
        pass
    
def binary(n):
    L=[]
    if n==0:
        return '0'
    while n!=0:
        if n%2==0:
            L.append('0')
        else:
            L.append('1')
        n=n/2
    return ''.join(L[::-1])

def ones(n):
    L=[]
    for i in list(str(n)):
        if i=='0':
            L.append('1')
        else:
            L.append('0')
    return ''.join(L)

def twos_from_ones(n):
    dec=int(str(n),2)+1
    two=binary(dec)
    return two
    
def process(L):
    try:
        answers=[]
        for i in L:
            if int(i)<0:
                i=abs(int(i))
            b=binary(int(i))
            if len(b)!=8:
                b='0'*(8-len(b))+b
            one=ones(b)
            number=twos_from_ones(one)
            answers.append(number)
        return answers
    except ValueError:
        pass
    
def show(L):
    display='\n'.join(L)
    print display
    return display

def saveFile(s):
    try:
        fo=open('Output.txt','w')
        fo.write(s)
        fo.close()
    except IOError:
        pass
    
try:
    s=raw_input()
    saveFile(show(process(getText(s))))
except:
    pass
