strList=[]
code=''
def Msg(s):
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
    return
def getText():
    global strList
    try:
        fr=open('FileIn.txt', 'r')
        strList=fr.read().split('\n')
        fr.close()
    except IOError:
        msg='File is not found or invalid file name'
        print msg
        Msg(msg)
        return False
    if len(strList)>=50:
        msg='Number of lines out of range'
        print msg
        Msg(msg)
        return False
    else:
        return True
def show():
    global code
    print code
    Msg(code)
    return
def encode():
    global code
    global strList
    import string
    codeList=[]
    alphaList=list(string.ascii_lowercase) #alphabet in lowercase
    for phrase in strList:
        codePhrase=''
        phrase=phrase.lower()
        if len(phrase)>20:
            codeList.append('Length of string out of range')
            continue
        for i in phrase:
            if i==' ':
                codePhrase+=' '
            else:
                try:
                    if alphaList.index(i)>=21:
                        codePhrase+=chr(5-(26-alphaList.index(i))+97)
                    else:
                        codePhrase+=chr(alphaList.index(i)+5+97)
                except ValueError:
                    codeList.append('Invalid string input for encoding')
                    break
        
        codeList.append(codePhrase)
    code='\n'.join(codeList)
    code=code.strip('\n')
if getText():
    encode()
    show()
    
    
                
                
            
            
        
    
    
