def getText():
    try:
        fo=open('FileIn.txt','r')
        n=int(fo.read())
        if not 0<n<10000:
            return 'invalid range of number'
        fo.close()
        return n
    except IOError:
        pass
    
def is_prime(x):
    status=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        return True

def process(n):
    answer=[]
    while True:
        if is_prime(n)==True and str(n)==str(n)[::-1]:
            answer.append(n)
        n+=1
        if len(answer)==5:
            break
    lines=[]
    display='Input N read from the file: %s\nFirst five palindromic primes > N:%s' %(n,' '.join(map(str,answer)))
    print display
    return display

def saveFile(s):
    try:
        fo=open('result.txt','w')
        fo.write(str(s))
        fo.close()
    except IOError:
        pass

try:
    saveFile(process(getText()))
except:
    pass
