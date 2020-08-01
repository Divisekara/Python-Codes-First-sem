#PA2 - 12 - Palindromic Primes

def getText():
    try:
        my_file = open("FileIn.txt","r")
        N = int(my_file.read())
        my_file.close()
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input! The input file must contain an integer N<10000."
    else:
        if 0<N<10000:
            return N
        else:
            print "Invalid Input! Input file must contain an integer N<10000."

def Show(x):
    p_primes=[]
    n=2
    y=str(x)
    while len(p_primes)<5:
        x+=1
        if int(str(x))==int(str(x)[::-1]):
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    break
            else:
                p_primes.append(x)
    pal_primes = " ".join(map(str,p_primes))
    my_string = "Input N read from the file: "+y+"\n"+"First five palindromic primes > N: "+pal_primes
    print my_string
    try:
        my_file_2 = open("Result.txt","w")
        my_file_2.write(my_string)
        my_file_2.close()
    except IOError:
        print "File Error!"
        
N = getText()
if N!=None:
    Show(N)
