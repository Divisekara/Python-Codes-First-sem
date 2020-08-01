def getText():
#getting the input
    try:
        fo=open('FileIn.txt','r')
        X=fo.read()
        fo.close()
    except IOError:
        print "File Error !"
    else:
        if X.isdigit():
            return X
        else:
            print "INVALID INPUT !"
    
def sum_productNumber(X):
#finding sum-product numbers
    SPNumbers=[]
    output=''
    for i in range(1,len(X)+1):
        for j in range(len(X)-i+1):
            N=X[j:j+i]
            Sum=0
            Product=1
            for d in N:
                Sum+=int(d)
                Product*=int(d)
            if Sum*Product==int(N):
                if N not in SPNumbers:
                    output+=N+" "
                    SPNumbers.append(N)
    if len(SPNumbers)==0:
        return "none"
    else:
        return output
    
def showResult(output):
#displaying and saving the output
    print output
    try:
        fo=open('result.txt','w')
        fo.write(output)
        fo.close()
    except IOError:
        print "File error !"

showResult(sum_productNumber(getText()))
