def getText():
    fo_in = open("FileIn.txt" , "r")
    global words
    words = []
    words_temp = []
    for i in range(50):
        words_temp.append(fo_in.readline())
    else:        
        for i in words_temp:
            try:
                if i[-1] == '\n':
                    if  i[:-1].isalpha():
                        words.append(i[:-1])
                else:
                    if  i.isalpha() and  i != '':
                        words.append(i)
                    else:
                        print "Invalid Input"
            except IndexError:
                continue
def show():
    vowels = ['a','e','i','o','u']
    
    global temp_words 
    temp_words = []
    temp1_words  = []
    global req_words
    req_words = []

    for i in words:
        count = 0
        for j in i:
            if j in vowels:
                count += 1
        else:
            if count != 0:
                temp1_words.append(i)
    else:
        for h in temp1_words:
            for i in vowels:
                count = 0
                for j in h:
                    if j == i:
                        count += 1
                else:
                    if count > 1:
                        break
            else:
                temp_words.append(h)
        else:
            for i in temp_words:
                temp_word_vowel = []
                for j in range(len(i)):
                    if i[j] in vowels:
                        temp_word_vowel.append(i[j])
                else:
                    for k in temp_word_vowel:
                        try:
                            if vowels.index(k) > vowels.index(temp_word_vowel[temp_word_vowel.index(k)+1]):
                                break
                        except IndexError:
                            continue
                    else:
                        req_words.append(i)
                            
                        
                            
                        
                    
    
                    
                
        
getText()
show()
print temp_words
print words
print req_words
        
