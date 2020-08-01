def getText():
    #get inputs
    try:
        fo=open('FileIn.txt','r')
        List=fo.read().split()
        fo.close()
    except IOError:
        print "File error !"
    else:
        for l in List:
            if not l.isalpha():
                print "not alphabetical !"
                return -1
                break
        else:
            return List
        
def LongestCommonSubstring(List):
    #finding longest substring
    output=''
    for word in List:
        A=True
        for i in range(len(word),0,-1):
            if A:
                for j in range(len(word)-i,0,-1):
                    if len(set(word[j-1:j+i].upper()))==2:
                        output+=word[j-1:j+i]+"\n"
                        A=False
                        break
    return output

def show(output):
    #di[lay and save output
    print output
    try:
        fo=open('result.txt','w')
        fo.write(output)
        fo.close()
    except IOError:
        print "File Error !"

            
show(LongestCommonSubstring(getText())) #calling functions within global state
