def getText(s):
    fo=open(s,'r')
    L=fo.read().split()
    fo.close()
    return L

def process(L):
    a=list(L[0])
    b=list(L[1])
    p=0
    if abs(len(a)-len(b))>0:
        p+=abs(len(a)-len(b))
    l=max(len(a),len(b))
    
    while True:
        if a==b:
            break
        for i in range(l):
            if a[i]!=b[i]:
                
                
            
def saveFile(s):
    fo=open('Output.txt','w')
    fo.write(s)
    fo.close()

process(getText(raw_input()))
