#PA2 - 01 - Repeating Letters.

words = []
def getText():
    global words
    try:
        my_file = open("FileIn.txt","r")
        words = (my_file.read()).split()
        my_file.close()
    except IOError:
        print "File Error!"
    else:
        word_numbers = []
        if len(words)<30:
            for i in range(len(words)):
                numbers = []
                if len(words[i])<20:
                    for j in list(set(words[i])):
                        numbers.append(words[i].count(j))
                    word_numbers.append(numbers)
                else:
                    print "Invalid Input! The length of a word must be less than 20 letters."
                    break
        else:
            print "Invalid Input! The number of words in Input file must be less than 30."
        if len(word_numbers)==len(words):
            return word_numbers   

def Show(x):
    letters = []
    output = ""
    for i in x:
        m=0
        for j in i:
            if j>=2:
                m+=1
        output += str(words[x.index(i)])+" - %d"%int(m)+"\n"
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
