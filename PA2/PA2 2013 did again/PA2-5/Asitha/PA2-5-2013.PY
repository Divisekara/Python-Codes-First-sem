def getText():
    FileOpen=open("FileIn.txt","r")
    L=FileOpen.read().split("\n")
    return L

def rename(L):
    renames=[]
    for i in L:
        answer=[]
        names=i.split()
        for j in names[:-1]:
            answer.append(j[0])
        answer.append(names[-1])
        renames.append(".".join(answer))
    return renames


def show(L):
    for i in L:
        print i
        
def saveFile(L):
    FileCreate=open("result.txt","w")
    for i in L:
        FileCreate.write(i)
        FileCreate.write("\n")
        

show(rename(getText()))
saveFile(rename(getText()))
            


