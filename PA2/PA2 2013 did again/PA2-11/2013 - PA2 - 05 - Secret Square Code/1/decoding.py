codeList=[]
decodeStr=''
def getText():
    global codeList
    try:
        fr=open('FileIn.txt', 'r')
        codeList=fr.read().split('_')
        fr.close()
        return
    except IOError:
        print 'File not found'
        return
def show():
    global decodeStr
    fw=open('result.txt', 'w')
    fw.write(decodeStr)
    print decodeStr
    fw.close()
    return
def codeWrong():
    fw=open('result.txt', 'w')
    fw.write('Wrong code')
    print 'Wrong code'
    fw.close()
    return
def decode():
    global decodeStr
    numStr='1'
    try:
        for code in codeList:
            for i in code:
                if i=='?':
                    if 
                    numStr.lstrip('1')
                    decodeStr+=chr(int(numStr))
                    numStr=''
                elif i=='#':
                    decodeStr+=numStr
                    numStr=''
                else:
                    numStr+=str(i)
            decodeStr+=' '
    except TypeError:
        codeWrong()
            
getText()
if decode():
    show()



