#PA2 - 02 - Min Max Interchange

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        numbers=fileOpen.read().split()
        fileOpen.close()
        numbers = map(int,numbers)
    except ValueError:
        print "Invalid Input!"
    except IOError:
        print "File Error!"
    else:
        if 7<len(numbers)<50:
            if 6<len(list(set(numbers))):
                return numbers
            else:
                print "Invalid Input!"
        else:
            print "Invalid Input!"

def swap_list(x):
    print x
    List=x[:]
    for i in range(3):
        a=min(x)
        b=max(x)
        z=List.index(a)
        y=List.index(b)
        (List[z],List[y])=(List[y],List[z])
        x.remove(a)
        x.remove(b)
    output = " ".join(map(str,List))
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
    show(swap_list(run))                                                                                   


