#PA2 - 05 - Secret Square Code

def getText():
    #To get text from input and check for any errors.
    try:
        my_file = open("FileIn.txt","r")
        words = (my_file.read()).split()
        N = int(words.pop(0))
        my_file.close()
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input! Number on the first line should be and integer."
    else:
        my_list=[]
        if N==len(words):
            if len(words)<1000:
                for i in words:
                    my_list.append(list(i))
                return my_list                
            else:
                print "Invalid Input! Number of words in second line must be less than 1000."
        else:
            print "Invalid Input! Number of words on second line must be equal to the number given in the first line of Input file."
            
def show(x):
    #To print the output on screen as well as write to a file.
    output=""
    for i in range(len(x)-1):
        if len(x[i])>len(x[i+1]):
            x[i+1].append(" ")
    for j in range(len(x)):
        for k in range(len(x[j])):
            output+=x[k][j]
    print output
    try:
        my_file_2 = open("Result.txt","w")
        my_file_2.write(output)
        my_file_2.close()
    except IOError:
        print "File Error!"

run = getText()   #To call functions in a global level                                                                                  
if run!=None:
    show(run)                                                                                   
