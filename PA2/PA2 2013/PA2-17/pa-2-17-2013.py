n=0
names=[]
ranks=[]
votes=0
def getText():
    L=[]
    with open("FileIn.txt","r") as FileRead:
        for line in FileRead:
            L.append(line[0:-1])
    print L
    FileRead.close()
    
    global n
    global names
    global ranks
    global votes
    
    n=int(L.pop(0)[0])
    for i in range(n):
        names.append(" ".join(L.pop(0)))
    print L
    for j in L:
        ranks.append(map(int,j.split()))
    votes=len(ranks)

def process():
    
    percentage=0
    
    result=[]
        
    for i in range(n):
        result.append(0)
            
    for i in ranks:
        rank=int(i.pop(0))-1
        x=result.pop(rank)
        result.insert(rank,x+1)

    #y=float(max(result))/votes
    print result


getText()
process()

    
    
