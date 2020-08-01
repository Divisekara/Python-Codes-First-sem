#PA2 - 01 - Same Number of '1' in Binary

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        num=int(fileOpen.read())
        fileOpen.close()
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input!"
    else:
        return num
        
def Dec_Bin(x):
    b_list = []
    while x!=0:
        b_list.append(x%2)
        x/=2
    b_list.reverse()
    return b_list

def Find(X):
    x = Dec_Bin(X)
    y = x.count(1)
    i = 1
    while True:
        X2 = X+i
        u = Dec_Bin(X2)
        z = u.count(1)
        if z==y:
            break
        i+=1
    output = "The answer: "+str(X2)
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
    show(Find(run))                                                                                   
    
