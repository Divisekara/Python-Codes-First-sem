def getText():
    try:
        fo=open('input_2.txt','r')
        L=map(int,fo.read().split('\n'))
        fo.close()
        L.pop(0)
        return L
    
    except ValueError:
        print 'invalid input. Enter integers only.'
        pass
    
    except IOError:
        print 'File not found.'
        pass      

def body(L):
    answers=[]
    for i in L:
        seq=[i]
        while True:
            if i==1:
                break
            else:
                if i%2==0:
                    i=i/2
                else:
                    i=i*3+1
                seq.append(i)
            
        answers.append(len(seq))
    return answers

def showResult(L):
    try:
        s="\n".join(map(str,L))
        print s
        
        fo=open('result.txt','w')
        fo.write(s)
        fo.close()
        
    except IOError:
        print 'File Error.'
        pass
    
    
    
showResult(body(getText()))

