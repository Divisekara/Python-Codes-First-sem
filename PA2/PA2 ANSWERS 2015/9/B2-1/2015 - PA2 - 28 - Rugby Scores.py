#PA2 - 28 - Rugby Scores

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        score=int(fileOpen.read())
        fileOpen.close()
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input!"
    else:
        if 0<score<100:
            return score
        else:
            print "Invalid Input!"

def scores(x):
    #To calculate the types of scoring methods
    if x==1 or x==2 or x==4:
        output = "INVALID SCORE"
    elif x==3:
        output = "Penalty/Drop Goals: 1"
    elif x==5:
        output = "Try: 1"
    elif x==7:
        output = "Try: 1"+"\n"+"Conversions: 1"
    elif x==8:
        output = "Try: 1"+"\n"+"Penalty/Drop Goals: 1"
    elif x==9:
        output = "Penalty/Drop Goals: 3"
    elif x==10:
        output = "Try: 1"+"\n"+"Conversions: 1"+"\n"+"Penalty/Drop Goals: 1"
    elif x==11:
        output = "Try: 1"+"\n"+"Penalty/Drop Goals: 2"
    elif x==12:
        output = "Try: 2"+"\n"+"Conversions: 1"
    else:
        Try=[]
        Con=[]
        Pen=[]
        for i in range(int(x**0.5)):
            for j in range(int(x**0.5)):
                for k in range(int(x**0.5)):
                    if 5*i+2*j+3*k==x:
                        if i>=j:
                            Try.append(i)
                            Con.append(j)
                            Pen.append(k)
        for i in range(len(Try)):
            if Pen[i]>0:
                if Try[i]==Con[i]:
                    output = "Try: %d"%Try[i]+"\n"+"Conversions: %d"%Con[i]+"\n"+"Penalty/Drop Goals: %d"%Pen[i]
                    break
                else:
                    output = "Try: %d"%Try[i]+"\n"+"Conversions: %d"%Con[i]+"\n"+"Penalty/Drop Goals: %d"%Pen[i]
            else:
                output = "Try: %d"%Try[i]+"\n"+"Conversions: %d"%Con[i]
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
    show(scores(run))                                                                                   


