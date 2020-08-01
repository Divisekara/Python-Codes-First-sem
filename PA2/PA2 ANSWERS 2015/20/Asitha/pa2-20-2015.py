def getText():
    try:
        fo=open("FileIn.txt","r")
        #fo=open("FileIn2.txt","r")
        L=fo.read().split("\n")
        fo.close()
        M=[]
        for i in L:
            x=map(int,i.split())
            M.append(x)
        return M
    except IOError:
        print "File Not Found"
        pass
    except ValueError:
        print "Invalid Input. Enter integers only"
        pass
    
def show(L):
    every_coordinates=[]
    for z in L:
        start=z[:2]
        end=z[2:]

        x_co=[]
        y_co=[]

        for i in range(start[0],end[0]+1):
            x_co.append(i)
        for j in range(start[1],end[1]+1):
            y_co.append(j)

        coordinates=[]

        for k in x_co:
            for l in y_co:
                x="".join(map(str,[k,l]))
                coordinates.append(x)
                
        every_coordinates.extend(coordinates)
        
    display=str(len(list(set(every_coordinates))))
    print display
    return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File Error."

try:
    saveFile(show(getText()))
except:
    print "Something worng with input. Try again"
    pass
