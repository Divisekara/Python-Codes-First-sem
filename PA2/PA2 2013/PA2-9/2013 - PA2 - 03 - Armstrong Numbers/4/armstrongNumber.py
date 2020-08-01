def getText():
    inputFile=open("FileIn.txt","r")
    L=inputFile.read().split()
    inputFile.close()

    if len(L)==2:
        for i in L:
            if not i.isdigit():
                print "TEXT FILE DOES NOT CONTAIN VALID INPUTS!\n"
                break
            else:
                M=int(L[0])
                N=int(L[1])
                if M<1000 and M<N<10000:
                    return [M,N]  
                else:
                    print "TEXT FILE DOES NOT CONTAIN VALID INPUTS!\n"
                    
    else:
        print "TEXT FILE DOES NOT CONTAIN VALID INPUTS!\n"

def showArmstrongNumbers(L):
    M, N = L[0], L[1]
    
    output1= "M and N :"+str(M)+" "+str(N)
    output2="Amstrong numbers between M and N: "
    print output1
    for n in range(M,N+1):
        digitList = list(str(n))
        power=len(digitList)
        Sum=0
        for d in digitList:
            Sum+=int(d)**power
        if Sum == n:
            output2+=str(n)+" "
    print output2
    openFile=open("result.txt","w")
    openFile.write(output1+"\n")
    openFile.write(output2)
    openFile.close()
    

#the main program calls the functions respectively getText(),showArmstrongNumbers(L) 
showArmstrongNumbers(getText())
