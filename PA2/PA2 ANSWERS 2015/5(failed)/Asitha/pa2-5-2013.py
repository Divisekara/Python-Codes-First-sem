N=0
def getText():
    try:
        fo=open("FileIn.txt","r")
        L=map(int,fo.readline().split())
        global N
        N=int(fo.readline())
        fo.close()
        print N
        print L
    except IOError:
        print "File not found"
        pass
    except ValueError:
        print "enter integers only."
        pass
    else:
        return L

#dominant number(highest number of times if same appears then
#smallest number is dominant)
#fixed consecutive numbers is an interval
    
def process(L):
    for i in range(len(L)-N+1):
        temp=L[i:i+N]
        times=[]
        for j in range(N):
            x=temp[j]
            y=temp.count(x)
            times.append(y)
        if times.count(max(times))>1:
               
            
            


process(getText())






