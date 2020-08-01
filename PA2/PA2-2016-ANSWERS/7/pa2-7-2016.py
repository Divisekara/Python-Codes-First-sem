def getText():
    try:
        fo=open('input_3.txt','r')
        L=fo.read().split('\n')
        fo.close()
        global n
        n=int(L.pop(-1))
        
    except IOError:
        print "File not found."
        pass
    else:
        M=list(L[0])

        if M[0].isalpha()==True and M[1].isalpha()==True and M[2].isdigit()==True and M[3].isdigit()==True and M[4].isalpha()==True and M[3].isdigit()==True:
            return M
        else:
            print "Invalid Input."
            pass

alpha=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ' )       

def showResult(M):
    try:
        x1=int(M[-1]) #number
        x2=M[-2] #alpha
        x3=int(M[-3]) #number
        x4=int(M[-4]) #number
        x5=M[-5] #alpha
        x6=M[-6] #alpha
        
        for i in range(n):
            if x1<9:
                x1+=1
            else:
                x1=0
                if x2!='Z':
                    x2=alpha[alpha.index(x2)+1]
                else:
                    x2='A'
                    if x3<9:
                        x3+=1
                    else:
                        x3=0
                        if x4<9:
                            x4+=1
                        else:
                            x4=0
                            if x5!='Z':
                                x5=alpha[alpha.index(x2)+1]
                            else:
                                x5='A'
                                if x6!='Z':
                                    x5=alpha[alpha.index(x2)+1]
                                else:
                                    print 'Ending of numbers.'
                                    break

        new=[x6,x5,x4,x3,x2,x1]
        s=''.join(map(str,new))
        print s

        fo=open('result.txt','w')
        fo.write(s)
        fo.close()
        
    except ValueError:
        print 'Invalid Input.'
        pass
    except IOError:
        print 'Invalid Input.'
        pass
        
try: 
    n=0
    showResult(getText())
except:
    print 'Program closed.'
