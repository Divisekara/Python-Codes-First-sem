"""A program to identify anagrams for given two words"""

def getText():
    "a function to read and evaluate a string file , FileIn.txt"

    fo_out = open("result.txt", "w")
    try:
        fo_in = open("FileIn.txt", "r")
    
        global word_1
        global word_2
        word_1 = fo_in.readline()[:-1]
        word_2 = fo_in.readline()

        if word_2 == "\n" or word_1 == "":                                                          #the program only accepts texts files without empty lines
            print "Input file must not contain empty lines or the text file is empty"
            fo_out.write("Input file must not contain empty lines or the text file is empty")
            return False
        
        elif not(word_1.isalpha()) or not(word_2.isalpha()) :                       #checks if words contain non alphabet characters
            print "Contains non alphabet characters"
            fo_out.write("Contains non alphabet characters")
            return False
        
        elif len(word_1) > 19 or len(word_2) >19:                                   #checks if words are longer than 19 characters
            print "Words are too long"
            fo_out.write("Words are too long")
            return False
        else:
            return True
    
    except IOError:
        print "No such file in Directory"
        fo_out.write("No such file i Directory")
        return False
    finally:
        fo_in.close()
        fo_out.close()
            
        
def show(w_1 , w_2):
    "a function to show if two given words are anagrams"
    
    with open("result.txt" , "w") as fo_out:
        if len(w_1) != len(w_2):                                                    #checks if the two words are not of same length
            print "No"                                                              #if so they aren't anagrams
            fo_out.write("No")
        else:
            w_1_list = list(w_1)
            w_2_list = list(w_2)

            if w_1_list.sort() == w_2_list.sort():                                  #checks if the two words have the same letters
                print "Yes"                                                         #if so they are anagrams
                fo_out.write("Yes")
            else:
                print "No"                                                          #if not they aren't anagrams
                fo_out.write("No")


            
if getText():                                                                       #the main program calls the getText func
    show(word_1, word_2)                                                            #calls the show func only if getTexts returns True
