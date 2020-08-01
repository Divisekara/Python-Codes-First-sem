def is_prime(x):
    isPrime=True
    if x==0 or x==1:
        return False
    else:    
        for i in range(2,int(x**.5)+1):
            if x%i==0:
                isPrime=False
                break
        return isPrime

def palindrome(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False

def getText():
    try:    
        FileRead=open("FileIn.txt","r")
        N=int(FileRead.read())
        FileRead.close()
    except ValueError:
        print "Non integer input"
        pass
    except IOError:
        print "File not found."
        pass
    else:
        if not 0<N<10000:
            print "Invalid N. Out of range."
        else:
            return N

def process(N):
    line1="Input N read form the file: " + str(N)
    palin_primes=[]
    n=1
    while n<=5:
        if is_prime(N)==True and palindrome(N)==True:
            palin_primes.append(N)
            n+=1
        line2="First five palindromic primes > N: " + " ".join(map(str,palin_primes))
        N+=1
    answer=line1+"\n"+line2
    print answer
    return answer

def saveFile(s):
    try:
        FileWrite=open("result.txt","w")
        FileWrite.write(s)
        FileWrite.close()
    except IOError:
        print "File Error"
        pass
    
saveFile(process(getText()))




 
