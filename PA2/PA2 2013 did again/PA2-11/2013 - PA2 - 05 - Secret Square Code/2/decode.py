width=0
S=''
EList=[]
def getText():
    global width
    global EList
    try:
        fr=open('FileIn.txt', 'r')
        width=int(fr.readline())
        para=fr.read()
        EList=para.split()
        fr.close()
        if len(EList)!=width:
            msg='Block width and the code does not match'
            print msg
            Msg(msg)
            return False
        elif len(para)>1000 or len(para)==0:
            msg='String length not in range'
            print msg
            Msg(msg)
            return False
        return True
    except IOError:
        msg='File not found or invalid file name/location'
        print msg
        Msg(msg)
        return False
    except ValueError:
        msg='Please input an integer for the width'
        print msg
        Msg(msg)
        return False
def show():
    global S
    print S
    Msg(S)
    return
def Msg(s):
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
    return
def decipher():
    global EList
    global S
    global width
    for i in range(len(EList[0])):
        for block in EList:
            try:
                S+=block[i]
            except IndexError:
                break
    return
if getText():
    decipher()
    show()
    
