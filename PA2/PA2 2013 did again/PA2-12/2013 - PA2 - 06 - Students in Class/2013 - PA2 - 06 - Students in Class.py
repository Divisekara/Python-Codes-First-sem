#PA2 - 05 - Secret Square Code.

def getText():
    try:
        my_file = open("FileIn.txt","r")
        words = (my_file.read()).split()
        my_file.close()
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input! Number on the first line should be and integer."
    else:
        students = []
        if len(words)%4==0:
            n = len(words)/4
            for i in range(n):
                temp_list=[]
                for j in range(4):
                    temp_list.append(words.pop(0))
                students.append(temp_list)
            for k in students:
                if len("".join(k))>=20:
                    print "Invalid Input! Length of a line must be less than 20."
            else:
                return students
        else:
            print "Invalid Input! Number of students in the class must be less than 50."                
                        
def Show(x):
    output=""
    names = []
    totals = []
    averages = []
    ranks = []
    for i in x:
        names.append(i.pop(0))
    for j in x:
        j = map(int,j)
        totals.append(j[0]+j[1]+j[2])
    for k in totals:
        averages.append(round(k/3.0,2))
    averages2 = averages[:]
    averages2.sort()
    averages2.reverse()
    for k in averages:
        ranks.append(averages2.index(k)+1)
    for i in range(3):
        output+=names[i]+" "+str(totals[i])+" "+str(averages[i])+" "+str(ranks[i])+"\n"
    print output
    try:
        my_file_2 = open("Result.txt","w")
        my_file_2.write(output)
        my_file_2.close()
    except IOError:
        print "File Error!"
        
run = getText()
if run!=None:
    Show(run)
