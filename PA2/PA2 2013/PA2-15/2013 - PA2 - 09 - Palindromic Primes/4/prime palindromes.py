N=0
palPrimes=''
def getText():
    global N
    try:
        fo=open('FileIn.txt', 'r')
        NList=fo.read().split()
        fo.close()
        if len(NList)!=1:
            Msg = 'Please insert one integer to the relevant file'
            print Msg
            msgWrite(Msg)
            return False
        elif int(NList[0])<0 or int(NList[0])>10000:
            Msg = 'N out of range' 
            print Msg
            msgWrite(Msg)
            return False
        else:
            N=NList[0]
            return True
    except ValueError:
        Msg = 'Please enter an intiger for the relevant file'
        print Msg
        msgWrite(Msg)
        return False
    except IOError:
        Msg = 'The file name is not valid or the file does not exist'
        print Msg
        msgWrite(Msg)
        return False
def showPalindromicPrimes():
    global N
    global string
    output='Input N read from the file: '+str(N)+'\n'+'First five palibdromic primes > N:'+string
    fw=open('result.txt', 'w')
    fw.write(output)
    fw.close()
    print output
    return
def msgWrite(msg):
    fw=open('result.txt', 'w')
    fw.write(msg)
    fw.close()
def isPrime(n):
    import math
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,int(math.ceil(math.sqrt(n)))+1):
            if n%i==0:
                return False
        else:
            return True
def isPalindrome(n):
    if len(str(n))==1:
        return True
    nlist=list(str(n))
    if len(str(nlist))%2!=0:
        nlist.pop(len(nlist)/2)
    n1=nlist[:len(nlist)/2]
    n2=nlist[len(nlist)/2:]
    n2.reverse()
    if n1==n2:
        return True
    else:
        return False
def findPalPrime(n):
    palPrimeList=[]
    if n%2==0:
        n+=1
    while True:
        if isPrime(n):
            if isPalindrome(n):
                palPrimeList.append(str(n))
        if len(palPrimeList)==5:
            break
        n+=1
    palPrimes=' '.join(palPrimeList)
    return palPrimes

if getText():
    string=findPalPrime(int(N))
    showPalindromicPrimes()
    
    
