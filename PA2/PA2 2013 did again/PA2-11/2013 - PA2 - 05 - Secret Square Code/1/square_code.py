''' a program to decode a message encoded in square code'''

def getText():
    'a function to read and get inputs from a text file'
    fo_out = open('result.txt' , 'w')
    try:
        fo_in = open('FileIn.txt', 'r')

        global width                                                                                    #reading the file and getting the rectangle width and the coded message
        width = fo_in.readline()[:-1]
        msg = fo_in.readline().split(" ")

        global msg_words
        msg_words = []
        if 0 < len(msg) < 1000:                                                                       #checking the validity of the inputs
            width = int(width)
            for i in msg:
                if i == '':
                    print "Message contains more than one space between words"
                    fo_out.write("Message contains more than one space between words")
                    return False
                else:
                    msg_words.append(i)
            else:
                return True
        else:
            fo_out.write("Invalid length of rectangle")
            print "Invalid length of rectangle"
            return False
            
    except IOError:
        fo_out.write("Input file not in directory")
        print "Input file not in directory"
        return False
    except ValueError:
        fo_out.write("Invalid length of rectangle")
        print "Invalid length of rectangle"
        return False

    finally:
        fo_in.close()
        fo_out.close()


def decoder(width, msg_words):
    'a function to decode an encoded message using square code'
    decod_msg_words = []                                                                #this list contains the decoded message words

    for i in range(width):
        line = ''
        for j in msg_words:                                                             #i_th letter of each row is taken and appended to a list
            try:
                line += j[i]
            except IndexError:
                continue
        else:
            decod_msg_words.append(line)
    else:
        return decod_msg_words
            
def show():
    'funtion to display the decoded message to the shell and to write it to a file'
    print ''.join(decoder(width, msg_words))
    fo_out  = open('result.txt' , 'w')
    fo_out.write(''.join(decoder(width, msg_words)))
    fo_out.close()

if getText():
    show()
