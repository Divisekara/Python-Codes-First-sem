def getText():
#getting inputs in prefered form
    try:
        fo=open('FileIn.txt','r')
        inputText=fo.read().split()
        fo.close()
        if len(inputText)==2:
            N=int(inputText[0])
            B=int(inputText[1])
            return(N,B)
        else:
            print "Exactly two inputs only !"
    except ValueError:
        print "Could not find an integer !"
    except IOError:
        print "File error !"

def findBinary(Tup):
#calculates the relavant binary and the expansion
    N=Tup[0]
    B=Tup[1]
    number=''
    expansion=''
    k=0
    while not(N<B-1):
        number+=str(N%B)
        N=N/B
        expansion+="%d*%d^%d + " % (N%B,B,k)
        k+=1
    number=number[::-1]   
    return number+" = "+expansion[0:-2]    
    
def show(output):
#printing and saving the output
    print output
    try:
        fo=open('result.txt','w')
        fo.write(output)
        fo.close()
    except IOError:
        print "File error !"

print getText()    
show(findBinary(getText())) #calling methods in global level
