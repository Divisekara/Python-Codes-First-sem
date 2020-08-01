def gettext():
    try:
        fileopen=open('FileIn.txt','r')
        inputs=fileopen.read().strip().split('\n')
        print inputs
    except IOError:
        print 'file reading error'
    else:
        fileopen.close()
        return inputs
inputs=gettext()
electors=int(inputs[0])
elec=inputs[1:electors+1]
ballots=[]
for i in inputs[electors+1:]:
    b=[]
    i=i.strip().split()
    for j in i:
        b.append(j)
    ballots.append(b)
for i in range(1,electors+1):
    ele=[]
    for j in range(1,electors+1):
        count=0
        for k in ballots:
            if str(j)==k[0]:
                count+=1
        ele.append(count)
    can=False
    for h in ele:
        if float(h)/sum(ele)>=0.5:
            print elec[ele.index(h)]
            can=True
    if not can:
        ele=map(int,ele)
        ind=ele.index(min(ele))+1
        for f in ballots:
            if f[0]==str(ind):
                ballots[ballots.index(f)].remove(str(ind))
    if can:
        break
            
        
