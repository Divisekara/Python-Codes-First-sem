#PA2 - 07 - Anagrams

def getText():
    try:
        my_file = open("FileIn.txt","r")
        words = (my_file.read()).split()
        my_file.close()
        words_list=[]
        for i in words:
            for j in i:
                words_list.append(j)
        words_list2 = words_list[:]
    except IOError:
        print "File Error!"
    else:
        ana_words=[]
        for i in range(2):
            temp_list=[]
            if len(words_list)%2==0 and (len(words_list)//2)<20:
                for j in range(len(words_list2)/2):
                    if words_list2[j].isalpha()==False:
                        print "Invalid Input! Input file must contain alphabetic letters!"
                    else:
                        temp_list.append(words_list.pop(0))
            ana_words.append(temp_list)
        if len(ana_words)==(len(words_list2)//len(ana_words[0])):
            return ana_words
                        
def Show(x):
    m=0
    for i in range(2):
        for j in range(len(x[i])):
            if x[i][j] in x[-i-1]:
                m+=1
    if m==len(x[1])*2:
        Output = "Yes"
        print Output
    else:
        Output = "No"
        print Output
    try:
        my_file_2=open("Result.txt","w")
        my_file_2.write(Output)
        my_file_2.close()
    except IOError:
        print "File Error!"

ana_list = getText()
if ana_list!=None:
    Show(ana_list)
