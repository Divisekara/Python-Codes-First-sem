students={}
resultList=[]
def getText():
    try:
        global students
        fr=open('FileIn.txt', 'r')
        while True:
            data=fr.readline()
            if len(data)>20:
                msg='Input line length out of range'
                print msg
                Msg(msg)
                return False
            data=data.split()
            if len(data)==0:
                break
            if len(data)!=4:
                msg='Input data or structure invalid'
                print msg
                Msg(msg)
                return False
            if not data[0].isalpha():
                msg='Invalid name in the input'
                print msg
                Msg(msg)
                return False
            marks=map(int,data[1:])
            for mark in marks:
                if mark>100 or mark<0:
                    msg='Input marks invalid'
                    print msg
                    Msg(msg)
                    return False
            students[data[0]]=marks
        if len(students)>50:
            msg='Number of students out of range'
            print msg
            Msg(msg)
            return False
        fr.close()
        return True
    except IOError:
        msg='Input file not found'
        print msg
        Msg(msg)
        return False
    except ValueError:
        msg='Input marks invalid'
        print msg
        Msg(msg)
        return False
        
def show():
    global resultList
    result='\n'.join(resultList).strip('\n')
    print result
    Msg(result)
    return
def Msg(s):
    fw=open('result.txt', 'w')
    fw.write(s)
    fw.close()
    return
def rank():
    global students
    total={}
    average={}
    totList=[]
    for student in students:
        tot=sum(students[student])
        avg=round(float(tot)/3,2)
        total[student]=tot
        average[student]=avg
        totList.append(tot)
    totList.sort()
    totList.reverse()
    rankList=[]
    for i in totList:
        for j in total:
            if total[j]==i:
                rankList.append(j)
                break
    for student in students:
        resultList.append(student+' '+str(total[student])+' '+str(average[student])+' '+str(rankList.index(student)+1))
    return
if getText():
    rank()
    show()        
        
        
