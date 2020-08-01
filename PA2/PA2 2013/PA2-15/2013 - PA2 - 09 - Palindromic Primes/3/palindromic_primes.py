def getText():
    'a function to read inputs from a text file'
    try:
        fo_out = open("result.txt" , "w")
        fo_in = open("FileIn.txt", "r")
        global N
        N = int(fo_in.read())

        if 0 < N < 10000 :
            return True
        else:
            print "N out of range"
            fo_out.write("N out of range")
            return False
    except IOError:
        print "File does not exist in the directory"
        fo_out.write("File does not exist in the directory")
    finally:
        fo_out.close()
        fo_in.close()

def isprime(x):
    'a function to determine prime numbers'
    if x <1 :
        return False
    elif x == 1:
        return True
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
        else:
            return True

def ispalindrome(x):
    'a function to determine palindromic numbers'
    str_x = str(x)
    rev_str_x = str_x[::-1]

    if str_x == rev_str_x :
        return True
    else:
        return False


def showPalindromicPrimes(N):
    'a function to show the first 5 Palindromic Primes greater than N'
    count = 0
    palindromic_primes = []
    temp_N = N
    while count < 5:
        temp_N += 1
        if isprime(temp_N) and ispalindrome(temp_N):
            palindromic_primes.append(str(temp_N))
            count += 1
            
    else:
        print "Input N read from file: %d" % N
        print "First five palindromic primes > N:", " ".join(palindromic_primes)

        fo_out = open("result.txt" , "w")

        fo_out.write("Input N read from file: %d" % N)
        fo_out.write("\nFirst five palindromic primes > N:",)
        fo_out.write(" ".join(palindromic_primes))

        fo_out.close()


if getText():
    showPalindromicPrimes(N)
        
        
    
            
                     
