def getText(s):
    fo=open(s,'r')
    L=fo.read().split('\n')
    fo.close()

    return L


def process(L):
    for i in L:
        M=i.split()
        y=M.pop()
        x=M.pop()
        N=M[0].strip('[').strip(']').split(',')
        P=N[::]
        new_list=[]
        for i in range(len(N)-1):
            if N[i]==y:
                b=i #
            if N[i]==x and N[i+1]!=y:
                a=N[i+1] #item
                if b!=None:
                    continue
                else:
                    p[
              
        


s=raw_input()
process(getText(s))
