def getText():
    try:
        FileOpen=open("FileIn.txt","r")
        L=FileOpen.read().split()
        return L
    except:
        print "File not found"
        pass
    
def compute(L):
    "Input a list of word and output the number of same letters appears in each word as a list"
    answer=[]
    for i in L:
        n=0
        for j in i:
            word = list(i)
            if word.count(j)>1:
                n += 1
                x=word.count(j)
                for k in range(x):
                    word.pop(k)             
                break
        answer.append(n)
    return answer

def show(words,numbers):
    lines = ""
    print words
    print numbers
    for i in range(len(words)):
        lines += words[i] + " - " + str(numbers[i]) + "\n"
    print lines
    return lines

def saveFile(x):
    "Input a string and save it in a file called result.txt"
    try:
        FileCreate=open("result.txt","w")
        FileCreate.write(x)
    except:
        print "Fie error."
        pass

saveFile(show(getText(),compute(getText())))




    
