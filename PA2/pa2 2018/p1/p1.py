def getText(s):
    try:
        fo=open(s,'r')
        L=fo.read().split('\n')
        fo.close()
        return L
    except IOError:
        pass
   
def binary(n):
    try:
        L=[]
        if n==0:
            return '0'
        while n!=0:
            if n%2==0:
                L.append('0')
            else:
                L.append('1')
            n=n/2
        b=''.join(L[::-1])
        return b
    except ValueError:
        pass
    
def process(L):
    lines=[]
    for i in L:
        line=[]
        for j in list(i):
            ascii=int(ord(j))
            b='0'+binary(ascii)
            if len(b)!=8:
                b='0'*(8-len(b))+b
            line.append(b)
        lines.append(' '.join(line))
    return lines

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
except ValueError:
    pass
