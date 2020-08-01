def getText():
    try:
        candidates=[]
        myList=[]
        with open('FileIn.txt','r') as fo:
            for line in fo:
                myList.append(line[0:-1])
        print myList
    except IOError:
        print "File error !"
    else:
        try:
            numOfCandidates=int(myList.pop(0))
            namesOfcandidates=[myList.pop(0) for i in range(numOfCandidates)]
            ballets=[]
            for b in myList:
                ballet=[]
                for i in b.split():
                    ballet.append(int(i))
                ballets.append(ballet)
            print (numOfCandidates,namesOfcandidates,ballets)
            return (numOfCandidates,namesOfcandidates,ballets)
                
        except ValueError:
            print "could not found preffered input(s)!"
        
def showWinner(Input):
    numOfCandidates=Input[0]
    namesOfcandidates=Input[1]
    ballets=Input[2]
    noOfBallets=len(ballets)
    myDictionary={}
    for i in range(numOfCandidates):
        myDictionary.update({i+1:0})
    print myDictionary

    output=''
    boolean=True
    for k in range(numOfCandidates):                    #k to count ballets
        if boolean:
            for key in myDictionary.keys():             #checking winner
                if myDictionary[key]*2>noOfBallets:
                    output+=namesOfcandidates[key-1]
                    print namesOfcandidates[key-1]
                    boolean=False

            if boolean:
                for b in ballets:                           #counting choices
                    if b[k]in myDictionary.keys():
                        myDictionary[b[k]]+=1
                #print myDictionary
                eliminatedCandidates=[]
                

            #print myDictionary         
            minVotes=min(myDictionary.values())
            if boolean:
                for key in myDictionary.keys():
                    if myDictionary[key]==minVotes:
                        eliminatedCandidates.append(key)
                print eliminatedCandidates
            
                for b in ballets:
                    if(b[k+1] not in eliminatedCandidates) and (b[k] in eliminatedCandidates):
                        myDictionary[b[k+1]]+=1
                        ballets.remove(b)
                        #print "ya"
                for e in eliminatedCandidates:
                    myDictionary.pop(e)               
    print myDictionary                      
    
    try:
        fo=open('result.txt','w')
        fo.write(output)
    except IOError:
        print "File error !"
    
showWinner(getText())

'''  for i in range(numOfCandidates):
        myDictionary.update({i+1:0})
    for b in ballets:                                   #counting ballets
        for i in range(numOfCandidates):                # ''
            myDictionary[i+1]+=(numOfCandidates-i)      # ''
    print myDictionary
    MaxVotes=max(myDictionary.values())
    print MaxVotes
    Winners=[]
    for i in myDictionary.keys():
        if myDictionary[i]==MaxVotes:
            Winners.append(namesOfcandidates[i-1])    
    output=""
    for w in Winners:
        output+=w+"\n"
    print output'''
