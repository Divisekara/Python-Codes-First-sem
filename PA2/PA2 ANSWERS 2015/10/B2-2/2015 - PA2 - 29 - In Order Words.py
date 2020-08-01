#PA2 - 29 - In Order Words

def getText():
#To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        words=fileOpen.read().split()
        fileOpen.close()
    except IOError:
        print "File Error!"
    else:
        if len(words)<1000:
            for i in words:
                if len(i)<20 and i.isalpha():
                    continue
                else:
                    print "Invalid Input!"
                    break
            else:
                return words
        else:
            print "Invalid Input!"

def In_order(x):
    #To check if each word is an inorder word
    List=[]
    List2 = []
    Inorder=[]
    for j in x:
        List.append(list(j))
    for i in x:
        j=list(i)
        j.sort()
        List2.append(j)
    for i in range(len(x)):
        if List[i]==List2[i]:
            Inorder.append("".join(List[i]))
    output=" ".join(Inorder)
    return output          

def show(output):
#To print the output on screen as well as write to a file.
    print output
    try:
        fileWrite=open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()   #To call functions in a global level                                                                                  
if run!=None:
    show(In_order(run))                                                                                   


