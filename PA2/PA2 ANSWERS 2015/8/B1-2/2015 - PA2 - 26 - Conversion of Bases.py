#PA2 - 26 - Conversion of Bases

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        numbers=fileOpen.read().split()
        fileOpen.close()
        if len(numbers)==2:
            B=int(numbers[-1])
            N=int(numbers[0])
        else:
            print "Invalid Input! Only 2 integers should be in the input file."
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input!"
    else:
        if 1<N<100000:
            if 1<B<10:
                return map(int,numbers)
            else:
                print "Invalid Input!"
        else:
            print "Invalid Input!"

def Conversion(x):
    #To convert Bases
    output=""
    factors=[]
    terms=[]
    B=int(x.pop(-1))
    N=int(x.pop(0))
    while N>1:
        factors.append(str(N%B))
        N=N/B
    factors.append("1")
    factors2=factors[:]
    factors.reverse()
    for j in range(len(factors)):
        terms.append("%s*%d^%d"%(factors2[j],B,j))
    output+="".join(factors)+" = "+" + ".join(terms)
    return output
          
def show(output):
    #To print the output on screen as well as write to a file.
    print output
    try:
        fileWrite=open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()                                                                                     
if run!=None:
    show(Conversion(run))                                                                                   


