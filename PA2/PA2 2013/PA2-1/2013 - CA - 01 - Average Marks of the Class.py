#CA - 01 - Average Marks of the Class

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        List=fileOpen.read().split()
        fileOpen.close()
        N=int(List.pop(0))
        M=int(List.pop(0))
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input!"
    else:
        Names=[]
        Marks=[]
        if 1<=N<=60:
            if 4<=M<=100:
                if len(List)%(M+1)==0:
                    for i in range(N):
                        Names.append(List.pop(0))
                        temp=[]
                        for j in range(M):
                            try:
                                if int(List[0])<=20:
                                    temp.append(int(List.pop(0)))
                                else:
                                    print "Invalid Input!"
                            except ValueError:
                                print "Invalid Input!"
                        Marks.append(temp)
                else:
                    print "Invalid Input!"
            else:
                print "Invalid Input!"
        else:
            print "Invalid Input!"
        if len(Names)==N:
            for i in Marks:
                if len(i)!=M:
                    print "Invalid Input!"
            else:
                Marks.append(Names)
                return Marks

def Avg(x):
    Names = x.pop()
    Avg=[]
    C_Tot=0
    for i in range(len(Names)):
        Sum=0
        for j in range(len(x[i])):
            Sum+=x[i][j]
        avg=round(Sum/float(len(x[i])),2)
        C_Tot+=avg
        Avg.append(avg)
    C_avg=round(C_Tot/float(len(Names)),2)
    output = "Class average: %.2f"%C_avg+"\n"
    for i in range(len(Avg)):
        output+="%s average: %.2f"%(Names[i],Avg[i])+"\n"
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
    show(Avg(run))  
