#PA2 - 10 - Unique Letters in a Word

def getText():
    try:
        my_file = open("FileIn.txt","r")
        word = str(my_file.read())
        my_file.close()
        words = word.split()
        for i in words:
            for j in i:
                if str(j).isalpha()==True:
                    continue
                else:
                    print "Invalid Input file! Input words should contain alphabetical letter!"
    except IOError:
        print "File Error!"
    else:
        if len(words)>=30:
            print "Invalid Input file! Number of words should be less than 30."
        else:
            for i in words:
                if len(str(i))>=20:
                    print "Invalid Input file! Length of each word should be less than 20."
            else:
                return words

def show(x):
    s_letters=[]
    n_words=[]
    final=""
    for i in x:
        for j in i:
            s_letters.append(j)
        for j in range(len(s_letters)):
            for k in range(j+1,len(s_letters)-1):
                if s_letters[k] == s_letters[j]:
                    s_letters.remove(s_letters[k])
        n_words.append("".join(s_letters))
        s_letters=[]
    for j in range(len(x)):
            final+= str(x[j])+" - "+str(len(n_words[j]))+"\n"
    print final
    try:
        my_file2 = open("Result.txt","w")
        my_file2.write(final)
        my_file2.close()
    except IOError:
        print "File Error!"
    
                
List = getText()
if List!=None:
    show(List)
