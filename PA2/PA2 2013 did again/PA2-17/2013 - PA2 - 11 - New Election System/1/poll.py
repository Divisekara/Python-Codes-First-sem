nameList=[]
pollList=[]
pollDict={}
winner=[]
N=0
def getText():
    global N
    global nameList
    global pollList
    try:
        fr=open('FileIn.txt', 'r')
    except IOError:
        display('File not found')
        return False
    N=fr.readline()
    n=0
    try:
        while n<int(N):
            nameList.append(fr.readline().strip())
            n+=1
    except ValueError:
        display('Invalid input for number of candidates')
        return False
    if len(nameList)!=int(N):
        display('Input number of candidates and input candidates do not match')
        return False
    while True:
        polls=fr.readline().strip().split()
        if len(polls)!=int(N) and len(polls)!=0:
            display('Invalid input for polls')
            return False
        elif len(polls)==0:
            break
        try:
            polls=map(int, polls)
        except ValueError:
            display('Invalid input')
            return False
        pollList.append(polls)
    return True
def showWinner():
    global winner
    winner='\n'.join(winner).strip('\n')
    display(winner)
    return
def display(s):
    print s
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
    return
def findWinner():
    global winner
    totPoll=0
    winnerPoll=0
    for name in nameList:
        pollDict[name]=0
    for NthVote in range(1,int(N)+1):
        for ballot in pollList:
            try:
                pollDict[nameList[int(ballot[NthVote-1])-1]]+=1
                totPoll+=1
            except KeyError:
                continue
        candidates=pollDict.copy()
        for candidate in candidates:
            if float(pollDict[candidate])/totPoll>0.5 :
                if pollDict[candidate]>winnerPoll :
                    winner=[candidate]
                elif pollDict[candidate]==winnerPoll :
                    winner.append(candidate)
        if len(winner)>0:
            break
        else:
            minm=min(pollDict.values())
            maxm=max(pollDict.values())
            if minm!=maxm:
                for cand in candidates:
                    if pollDict[cand]==minm:
                        totPoll-=pollDict[cand]
                        del(pollDict[cand])
    return
if getText():
    findWinner()
    showWinner()
            
    
        
        
