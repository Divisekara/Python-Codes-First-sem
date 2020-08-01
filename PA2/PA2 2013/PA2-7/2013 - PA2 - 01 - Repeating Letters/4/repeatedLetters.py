def getText(text):
    readContent=''
    try:
        fileOpen=open(text,"r")
        readContent=fileOpen.read()
        fileOpen.close()
    except:
        print "File Error!"
    return readContent


def show(text):
    List=text.split()
    L=len(List)
    output=""
    if L<30:
        for i in range(0,L):
            if len(List[i])<20:
                letters=list(List[i])
                letterSet=list(set(list(List[i])))
                repeated=0
                for l in letterSet:
                    count=0
                    for j in range(0,len(letters)):
                        if l==List[i][j]:
                            count+=1
                    if count>1:
                        repeated+=1
                output+=List[i]+" - "+str(repeated)+"\n"       
            else:
                print "Length of a word must be less than 20!"
                break
        print output
        try:
            fileOpen=open("result.txt","w")
            fileOpen.write(output)
            fileOpen.close()
        except:
            print "File Error!"
    else:
        print "Only 30 words allowed!"
text=getText("FileIn.txt") 

if text!=None:
    show(text)

