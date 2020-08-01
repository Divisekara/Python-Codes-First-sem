def getText():
    try:
        FileRead=open("FileIn.txt","r")
        L=FileRead.read().split()
        FileRead.close()
    except IOError:
        print "File not found"
        pass
    else:
        if not len(L)<30:
            print "Number of words in file should be less than 30."
        else:
            for i in L:
                if not len(i)<20:
                    break
            else:
                return L

def process(L):
    answers=[]
    for i in L:
        word=list(i)
        letters=len(word)
        for j in i:
            n=word.count(j)
            if n>1:
                letters -= n-1
            for i in range(n):
                word.remove(j)
        answers.append(letters)
    return answers

def show(words,answers):
    n=len(words)
    lines=[]
    for i in range(n):
        line = words[i] + " - " + str(answers[i])
        lines.append(line)
    display= "\n".join(lines)
    print display
    return display

def saveFile(s):
    try:
        FileCreate=open("result.txt","w")
        FileCreate.write(s)
        FileCreate.close()
    except IOError:
        print "File error."
        pass

try:
    saveFile(show(getText(),process(getText())))
except:
    print "something went wront"
