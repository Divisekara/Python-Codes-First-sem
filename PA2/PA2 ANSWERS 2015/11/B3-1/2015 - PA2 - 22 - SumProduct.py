#PA2 - 22 - Sumproduct

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        number=int(fileOpen.read())
        fileOpen.close()
    except ValueError:
        print "Invalid Input!"
    except IOError:
        print "File Error!"
    else:
        if 0<=len(str(number))<=100:
            return number
        else:
            print "Invalid Input!"

def SumProduct(x):
    #To calculate the sumproducts
    sumproducts = []
    n = len(str(x))
    for i in range(n):
        for j in range(i,n+1):
            if i == j:
                continue
            else:
                Total=0
                Product=1
                m = str(x)[i:j]
                for k in str(m):
                    Total+=int(k)
                    Product*=int(k)
                if Total*Product==int(m):
                    sumproducts.append(m)
    sumproducts = list(set(sumproducts))
    if sumproducts!=[]:
        final = " ".join(sumproducts)
        return final
    else:
        return "none"

def show(output):
    #To print the output on screen as well as write to a file.
    print output
    try:
        fileWrite=open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()   #To call functions in a global level                                                                                  
if run!=None:
    show(SumProduct(run))                                                                                   


