#CA - 06 - Permuterms

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        words=fileOpen.read().split()
        fileOpen.close()
    except IOError:
        print "File Error!"
    else:
        if len(words)<50:
            for i in words:
                if len(i)>=20:
                    print "Invalid Input!"
                    break
            else:
                words = map(str,words)
                for i in range(len(words)):
                    words[i]=list(words[i])
                    words[i].append("$")
                return words
        else:
            print "Invalid Input!"

def permuterms(x):
    y=x[:]
    output=""
    for i in range(len(x)):
        out=""
        for j in range(len(x[i])-1):
            out+="".join(y[i])+" "
            z=y[i].pop(0)
            y[i].append(z)
        output+=out+"\n"
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
    show(permuterms(run))           
