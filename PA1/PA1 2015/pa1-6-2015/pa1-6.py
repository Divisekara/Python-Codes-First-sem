alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    try:
        letter = raw_input("Enter letter:")
        a = ord(letter)
    except TypeError:
        print "Invalid Input. Enter a letter in English alphabet.\n"
    except ValueError:
        print "Invalid Input. Enter a letter in English alphabet.\n "
    except:
        print "Try witha valid Input."
    else:
        if 65<=a<=90:
            i=a-64
        elif 97<=a<=122:
            i = a-96
        else:
            print "Invalid Input! Enter any uppercase or lowercase letter in English alphabet."
            continue
        print "\n"
        
        for n in range(1,i+1):
            for x in range(i-n):
                print "",
            if n==1:
                print alphabet[n-1]
                continue
            print "%s%s"%(alphabet[:n],alphabet[n-2::-1])

        for n in range(1,i):
            for x in range(n):
                print "",
            if n==i-1:
                print alphabet[i-n-1]
                continue
            print "%s%s"%(alphabet[:i-n],alphabet[i-n-2::-1])
        print "\n"
        
        while True:
            like=raw_input("Do you want to continue (y/n):")
            z=0
            if like=='y':
                break
            elif like=='n':
                z=1
                break
            else:
                print "Enter 'y' or 'n'"
                continue
        if z==1:
            print "good bye"
            break
