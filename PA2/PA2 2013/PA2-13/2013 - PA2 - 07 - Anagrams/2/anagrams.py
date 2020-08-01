result=''
wordList=[]
def getText():
    global wordList
    try:
        fr=open('FileIn.txt', 'r')
        wordList=fr.read().split('\n')
        fr.close()
        return True
    except IOError:
        msg='File not found or invalid file name'
        print msg
        Msg(msg)
        return False
def show():
    global result
    print result
    Msg(result)
    return
def isAnagram(word1,word2):
    word1_,word2_=list(word1),list(word2)
    word1_.sort()
    word2_.sort()
    if word1_==word2_:
        return True
    else:
        return False
def Msg(s):
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
    return
if getText():
    if len(wordList)!=2:
        msg='Two and only two words should be input'
        print msg
        Msg(msg)
    elif  not(wordList[0].isalpha() and wordList[1].isalpha()):
        msg='Words should be provided as inputs'
        print msg
        Msg(msg)
    else:
        if isAnagram(wordList[0],wordList[1]):
            result='Yes'
        else:
            result='No'
        show()
    
