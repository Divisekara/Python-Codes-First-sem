def getText():
    FileOpen=open("FileIn.txt","r")
    L=FileOpen.read().split("\n")
    N=L.pop(0)
    FileOpen.close()
    return N,L



print getText()[1]


    
