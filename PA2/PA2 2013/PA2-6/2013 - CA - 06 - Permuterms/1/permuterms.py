def getText():
    try:
        fo_in = open("FileIn.txt","r")
        fo_out = open("result.txt","w")
        
        global word_list
        word_list = []
        word_list_temp = fo_in.read().split("\n")
        if len(word_list_temp) <50:
            for word in word_list_temp:
                if word != '':
                    if len(word) <20:
                        if word[-1] == "\n":
                            word_list.append(word[:-1] + "$")
                        else:
                            word_list.append(word + "$")
                    else:
                        print "Inputs are too long"
                        fo_out.write( "Inputs are too long")
                        break
                else:
                    continue
            else:
                return True
        else:
            print "Too much inputs"
            fo_out.write("Too much inputs")
    except IOError:
        print "file not in directory"
        fo_out.write("file not in directory")
    finally:
        fo_in.close()
        fo_out.close()
        

def show():
    fo_out = open("result.txt" , "w")
    permuterms_list = []
    for i in word_list:
        permuterms = [i]
        word_edit = i
        for j in range(len(i)-2):
            word_edit = word_edit[1:] + word_edit[0]
            permuterms.append(word_edit)
        else:
            permuterms_list.append(permuterms)
    else:
        for i in permuterms_list:
            for j in i:
                print j,
                fo_out.write(j+" ")
            else:
                print ''
                fo_out.write("\n")

            
if getText():
    show()
