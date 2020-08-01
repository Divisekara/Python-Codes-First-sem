#PA2 - 27 - Longest Common Substring

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen = open("FileIn.txt","r")                                                         
        words = (fileOpen.read()).split()
        fileOpen.close()
    except IOError:
        print "File Error!"
    else:
        if 0<=len(words)<=10:
            for i in words:
                if i.isalpha()==True:
                    return words
                else:
                    print "Invalid Input! Input file must contain alphabetical strings."
                    break
        else:
            print "Invalid Input! Input file must contain less than or equal to 20 strings only."
        
def getSubstring(x):
    #Find the longest substring
    output = ""
    for i in x:
        A=True
        for k in range(len(i),0,-1):
            if A:
                for j in range(len(i)-k,0,-1):
                    if len(set(i[j-1:j+k].lower()))==2:
                        output+=i[j-1:j+k]+"\n"
                        A=False
                        break
    return output

def show(output):
    #To print the output on screen as well as write to a file.
    print output
    try:
        fileWrite = open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()                                                                                     
if run!=None:
    show(getSubstring(run))                                                                                   


