N=0
matrix=[]
def getText():
    try:
        fo=open("FileIn.txt","r")
        L=[]
        while True:
            L.append(fo.readline().split())
            if L[-1]==[]:
                L.pop(-1)
                break
        fo.close()
    except IOError:
        print "File not found"
        pass
    else:
        try:
            global N
            global matrix
            N=int(L.pop(0)[0])
            if not 3<=N<=20:
                print "Out of range input."
            else:                
                for i in L:
                    matrix.append(map(int,i))
        except ValueError:
            print "Enter integers only."
            pass

def take_surrounding(i,j):
    total=0
    n=0
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            if k==-1 or l==-1:
                continue
            try:
                total+=matrix[k][l]
            except IndexError:
                pass
            else:
                n=n+1
    return total/n

def process():
    solution=[]
    for i in range(N):
        row=[]
        for j in range(N):
            row.append(take_surrounding(i,j))
        solution.append(row)
    return solution

def show(L):
    lines=[]
    for i in L:
        row=" ".join(map(str,i))
        lines.append(row)
    display="\n".join(lines)
    print display
    return display

def saveFile(s):
    try:
        fc=open("result.txt","w")
        fc.write(s)
        fc.close()
    except IOError:
        print "File Error."
        pass
try:
    getText()
    saveFile(show(process()))
except:
    print "Something went wrong."
    pass
