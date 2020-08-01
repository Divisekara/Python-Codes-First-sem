strList=[]
result=''
resultList=[]
def getText():
    global strList
    try:
        fr=open('FileIn.txt', 'r')
        strList=fr.read().split('\n')
        fr.close()
    except IOError:
        msg='File is not available or invalid file name'
        print msg
        Msg(masg)
    strList.pop()
    if len(strList)>=50:
        msg='Number of strings out of range'
        print msg
        Masg(msg)
        return False
    return True
def Msg(s):
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
def show():
    global result
    print result
    fw=open('result.txt', 'w')
    fw.write(result)
    fw.close()
def isPalindrome(s): #useless
    s1=list(s[:len(s)/2])
    s2=list(s[len(s)/2:])
    s2.reverse()
    if s1==s2:
        return True
    else:
        return False
if getText():
    for string in strList:
        if len(string)>=20:
            resultList.append('String length out of range')
            continue
        else:
            for i in string:
                try:
                    if i==string[string.index(i)+1]:
                        resultList.append('yes')
                        break
                except IndexError:
                    continue
            else:
                resultList.append('no')
    result='\n'.join(resultList)
    result.strip('\n')
    show()
