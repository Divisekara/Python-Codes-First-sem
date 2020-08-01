def getText():
    try:
        fo_in = open("FileIn.txt" , "r")
        fo_out = open("result.txt", "w")

        global word_list
        word_list = []
        word_list_temp = fo_in.read().split()

        if len(word_list_temp) <30:
            for i in word_list_temp:
                    if len(i) <20:
                        if i.isalpha():
                                word_list.append(i)
                        else:
                            print "One or more words contain non alphabet characters"
                            fo_out.write("One or more words contain non alphabet characters")
                            return False
                    else:
                        print "word/s is/are too long"
                        fo_out.write("word/s is/are too long")
                        return False
            else:
                return True
        else:
            print "Too many words"
            fo_out.write("Too many words")
            return False
    except IOError:
        print "No Input File in the directory"
        fo_out.write("No Input File in the directory")
    finally:
        fo_out.close()
        fo_in.close()

def repeated(i):
    rep_list  = []
    for j in i:
        j_count = 0
        for h in i:
            if j == h:
                j_count+= 1
                if j_count> 1:
                    if j not in rep_list:
                        rep_list.append(j)
                        break
                    else:
                        continue
                    
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        return len(rep_list)

def show():
    fo_out = open("result.txt" , "w")
    non_sim_lets_list = []
    for i in word_list:
        print i + " - " + "%d"%repeated(i)
        fo_out.write(i + " - " + "%d"%repeated(i)+"\n")
    else:
        fo_out.close()


    
if getText():
    show()
    
