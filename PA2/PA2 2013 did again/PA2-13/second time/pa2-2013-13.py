def getText():
    try:
        fo=open('FileIn.txt','r')
        L=fo.read().split()
        fo.close()
        return L
    except IOError:
        pass
    
def process(L):
    word1=selection_sort(list(L[0]))
    word2=selection_sort(list(L[1]))
    if word1==word2:
        status= 'yes'
    else:
        status= 'no'
    print status
    return status

def saveFile(s):
    try:
        fo=open('result.txt','w')
        fo.write(s)
        fo.close()
    except IOError:
        pass
    
def selection_sort(L):
    for i in range(0,len(L)-1):
        min_index=i
        for j in range(i+1,len(L)):
            if L[min_index]>L[j]:
                min_index=j
        if min_index!=i:
            L[i],L[min_index]=L[min_index],L[i]
    return L

try:
    saveFile(process(getText()))       
except:
    pass
