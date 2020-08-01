#PA2 - 23 - 90 Degress String Rotation

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        words=fileOpen.read().split()
        fileOpen.close()
    except IOError:
        print "File Error!"
    else:
        lens=[]
        for i in words:
            lens.append(len(i))
        n=max(lens)
        my_list = []
        for j in words:
            temp_list=[]
            if j.isalpha()==True:
                for k in j:
                    temp_list.append(str(k))
            else:
                print "Invalid Input!"
                break
            my_list.append(temp_list)
        if len(my_list)==len(words):
            my_list.append(n)
            return my_list
        
def Rotator(x):
    #To rotate the strings
    n=x.pop(-1)
    for i in x:
        while len(i)<n:
            i.append(" ")
    output=""
    for j in range(n):
        for k in range(len(x)):
            output+=x[k][j]
        output+="\n"
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
    show(Rotator(run))                                                                                   


