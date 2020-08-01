def getText():#Reading the file to get the data.
    try:
        fileOpen=open("FileIn.txt","r")
        L=fileOpen.read().split()
        fileOpen.close()
        N=int(L.pop(0))   ## number of students
        M=int(L.pop(0))   ## number of subjects
    except ValueError: print "Invalid Input.\n" 
    except IOError:    print "File not found."
    else:
        Names=[]
        Marks=[]
        if 4<=M<=100 and 1<=N<=60 and len(L)%(M+1)==0: #conditions and Input errors.
            for i in range(N):
                temp=[]
                Names.append(L.pop(0))
                for j in range(M):
                    try:
                        if int(L[0])<=20: temp.append(int(L.pop(0))) 
                        else: print "Invalid Input."
                    except ValueError: print "Invalid Input."
                Marks.append(temp)                  
        else: print "Invalid Input.\n"
        for i in Marks:
            if len(i)==M and len(Names)==N: return [Names,Marks] #Returning lists , Names and Marks as output
            else:print "Invalid Input.\n"

def process(x):#doing the procceses of finding the averages.
    Names=x[0]
    Marks=x[1]
    avg=[]
    total=0
    for i in range(len(Names)):
        sum_=0
        for j in range(len(Marks[i])):
            sum_+=Marks[i][j]
        average=round(sum_/float(len(Marks[i])),2)
        avg.append(average)
        total+=sum_
    last_average=round(float(total)/(len(Names)*len(Marks[i])),2)
    return [avg,last_average,Names]
    #Returning averages of student and class averages and
    #names of the students.

def show(x):#In order to print the output.
    avg=x[0]
    last_average=x[1]
    Names=x[2]
    line="Class average: %.2f"%(last_average) + "\n"
    for i in range(len(avg)):
        line=line + "%s average: %.2f"%(Names[i],avg[i]) + "\n"
    print line #printing the output without syntax "print"
    return line #just returning the output to be used.

def saveFile(x):#In order to write to a file
    try:
        if x!=None:
            fileCreate=open("Result.txt","w")
            fileCreate.write(x)
            fileCreate.close()
        else:
            pass
    except IOError:
        print "File Error.\n"

###Printing the output as well
###running the saveFile function to create a file.
saveFile(show(process(getText())))
