"""A program to identify if a word contains even length palindromes in it"""

def getText():
    "a function to read and evaluate a string file , FileIn.txt"

    fo_out = open("result.txt", "w")
    try:
        fo_in = open("FileIn.txt", "r")
        global word_list
        word_list = []
        word_count = 0
        break_loop = 0
        while break_loop == 0:                                                      #a loop that continues till break_loop == 0
            for line in fo_in:
                if word_count > 49:                                                 #checks if the file has less than 50 lines
                    print "Input file contains more than 49 lines"
                    fo_out.write("Input file contains more than 49 lines")
                    break_loop = 1
                    break
                elif len(line) > 19:                                                #checks if a line has less than 20 characters
                    print "Input file has words longer than 20 characters"
                    fo_out.write("Input file has words longer than 20 characters")
                    break_loop = 1
                    break
                else:
                    if len(line) == 0:                                              #checks for empty lines
                        print "Input file contains empty lines"
                        fo_out.write("Input file contains empty lines")
                        break_loop = 1
                        break
                    else:
                        if line[-1] == '\n':
                            word_list.append(line[:-1])
                        else:
                            word_list.append(line)
                        word_count += 1
            else:
                break_loop = 1
                return True
            
                        
    
    except IOError:
        print "No such file in Directory"
        fo_out.write("No such file i Directory")
        return False
    finally:
        fo_in.close()
        fo_out.close()




def palindrome(word):
    "a function a to determine a palindromic word"
    word_rev = word[::-1]                                                           #a palindrome reads the same backwards
    if word == word_rev:
        return True
    else:
        return False

def contains_even_palin(word):
    "a function to evaluate if a word has even length palindromic words in them"
    for i in range(2, len(word),2):                                                 #take even lengthed parts of the word 
        for j in range(len(word)-1):
            if palindrome(word[j:j+i]):                                             #and checks if that part is a palindrome
                return True
            else:
                continue
            


def show(w_list):
        "a function to show whether a list of words contains even length a palindromic words in each word"
        fo_out = open("result.txt" , "w")
        for word in w_list:
            if contains_even_palin(word):
                print "yes"
                fo_out.write("yes\n")
            else:
                print "no"
                fo_out.write("no\n")
        else:
            fo_out.close()
            return
if getText():
    show(word_list)
