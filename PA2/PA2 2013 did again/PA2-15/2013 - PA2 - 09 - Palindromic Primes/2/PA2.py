A=[]
a=0
b=0
def getText():
    global b
    global a
    try:
        filop=open('PA2.txt','r+')
        strnn=filop.read()
        num=float(strnn)
        if num%1!=0:
            print 'not an integer input but a float'
            a=1
        num=int(num)
        b=num
    except IOError:
        print 'no file found'
        a=1
    except ValueError:
        print 'non integer input of proper order'
        a=1
    except:
        print 'invalid input'

getText()
print a
print b
c=b

def showPalindromicPrimes():
    import math
    global b
    global A
    global c
    while 1:
        bb=b
        num=int(math.sqrt(bb))
        for fact in range(num,0,-1):
            if bb%fact==0:
                break
        if fact==1:
            liss=list(str(bb))
            if liss==liss[-1::-1]:
                A.append(bb)
        if len(A)==5:
            break
        b+=1
    print 'Input N read from file: %d'%(c)
    print 'First Five Palindromic primes >N: ',
    fileop2=open('PA2out.txt','wb')
    fileop2.write('Input N read from file: %d '%(c))
    fileop2.write('\n')
    fileop2.write('First Five Palindromic primes >N: ')
    for x in A:
        print '%d '%(x),
        fileop2.write('%d '%(x))
    fileop2.close()
getText()
if a==0:
    showPalindromicPrimes()
            
            
            

        

        
    
