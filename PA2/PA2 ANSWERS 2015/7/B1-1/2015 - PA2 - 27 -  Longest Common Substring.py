#PA2 - 27 - Longest Common Substring

def getText():
#To get text from input and check for any errors.
    try:
        fileOpen = open("FileIn.txt","r")                                                         
        words = (fileOpen.read()).split()
        fileOpen.close()
    except IOError:
        print "File Error!"
    else:
        words_list=[]
        if 0<=len(words)<=10:
            for i in range(len(words)):
                temp_list = []
                for j in words[i]:
                    temp_list.append(j)
                words_list.append(temp_list)
                print words_list
            return words_list
        else:
            print "Invalid Input! Input file must contain less than or equal to 20 strings only."
        

def show(x):
#To print the output on screen as well as write to a file.
    output = ""
    substrings = []
    for i in x:
        substrings2 = []
        for j in range(len(i)):
            for k in range(j,len(i)+1):
                if j==k:
                    continue
                else:
                    subs = i[j:k]
                    subs2 = ("".join(subs)).lower()
                    if len(list(set(subs2)))==2:
                        substrings2.append(subs)
        substrings.append(substrings2)
    final = []
    for i in substrings:
        temp_list=[]
        nums=[]
        for k in i:
            nums.append(len(k))
        n=max(nums)
        for j in i:
           if len(j)==n:
                temp_list.append(j)
        final.append(temp_list.pop(-1))
    for j in final:
        output+="".join(j)+"\n"
    print output
    try:
        fileWrite = open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()                                                                                     
if run!=None:
    show(run)                                                                                   


