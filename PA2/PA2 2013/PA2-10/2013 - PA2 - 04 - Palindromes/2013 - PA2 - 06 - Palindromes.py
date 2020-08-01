#PA2 - 06 - Palindromes

def getText():
    try:
        my_file = open("FileIn.txt","r")
        words = (my_file.read()).split()
        my_file.close()
        words_list=[]
        for i in words:
            temp_list=[]
            for j in i:
                temp_list.append(str(j))
            words_list.append(temp_list)                   
    except IOError:
        print "File Error!"
    else:
        if len(words_list)<50:
            for i in words_list:
                if len(i)<20:
                    return words_list
                else:
                    print "Invalid Input! Length of each line of Input file must be less than 20."
        else:
            print "Inavlid Input! Number of lines in input file must be less than 50."
            
                        
def Show(x):
    Output=""
    for i in x:
        if str("".join(i))==str("".join(i))[::-1]:
            if len(i)%2==0:
                Output+="yes"+"\n"
            else:
                Output+="no"+"\n"
        else:
            for j in range(len(i)):
                if j==len(i)-1:
                    continue
                else:
                    if i[j]==i[j+1]:
                        Output+="yes"+"\n"
                        break
            else:
                Output+="no"+"\n"
                
    print Output
    
    try:
        my_file_2=open("Result.txt","w")
        my_file_2.write(Output)
        my_file_2.close()
    except IOError:
        print "File Error!"

pal_list = getText()
if pal_list!=None:
    Show(pal_list)
