wordList=[]
resultDict={}
def getText():
    global wordList
    try:
        fr=open('FileIn.txt', 'r')
        while True:
            word=fr.readline().strip()
            if word=='':
                break
            if not word.isalpha():
                display('Invalid input for words')
                return False
            if len(word)>20:
                display('Length of input word out of range')
                return False
            wordList.append(word)
        if len(wordList)>20:
            display('Input word list out of range')
            return False
        return True
    except IOError:
        display('File not found')
def show():
    global resultDict
    result=''
    for word in resultDict:
        result+=word+' - '+str(resultDict[word])+'\n'
    result.strip('\n')
    display(result)
    return
def count(s):
    n=0
    letters=set(s)
    word=list(s)
    for let in letters:
        try:
            k=word.pop(word.index(let))
            if word.index(k)+1:
                n+=1
        except ValueError:
            continue
        except IndexError:
            continue
    return n
def display(s):
    print s
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
    return
if getText():
    for word in wordList:
        resultDict[word]=count(word)
    show()
        
    
        
        
    
