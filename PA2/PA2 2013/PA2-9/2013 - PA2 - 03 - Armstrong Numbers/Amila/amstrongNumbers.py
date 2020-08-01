def getText():
#get text and check their validity
    try:
        fileOpen=open('FileIn.txt','r')                                                         #openning and reading the file content
        readText=fileOpen.read()
        fileOpen.close()
    except IOError:
        print "File error !"
    else:
        List=readText.split()

        if len(List)==2:                                                                        #checking for preffered inputs
            try:
                M=int(List[0])
                N=int(List[1])
            except ValueError:
                print "Some are not integers !"
            else:
                if 0<M<1000 and M<N<10000:
                    return [M,N]
                else:
                    print "Integers were not in preffered way !"
        else:
            print "Text is not in the preffered manner !"

def armstongNumbers(L):
#finding and printing and writing armstrong numbers
    M=L[0]
    N=L[1]
    armstrongNumbers=''
    for n in range(M,N+1):                                                                      #finding armstrong numbers between M and N
        total=0
        digitSeq=str(n)
        power=len(digitSeq)
        for d  in digitSeq:
            total+=int(d)**power
        if n==total:
            armstrongNumbers+=str(n)+" "

    output="M and N: "+str(M)+" "+str(N)+"\nArmstong numbers between M and N:"+armstrongNumbers 
    print output

    try:
        fileWrite=open('result.txt','w')                                                        #writing output into a file
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "FileError"

x=getText()                                                                                     #calling get text funtion
if x!=None:
    armstongNumbers(getText())                                                                  #calling armstongNumbers function                   


