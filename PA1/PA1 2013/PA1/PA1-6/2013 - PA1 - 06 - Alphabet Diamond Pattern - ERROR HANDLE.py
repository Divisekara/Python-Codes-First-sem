#PA1 - 6 - Alphabet Diamond Pattern

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    letter = raw_input("Enter letter: ")
    a = ord(letter)
    if 65<=a<=90:
        i = a-64
    elif 97<=a<=122:
        i = a-96
    else:
        print "Invalid input! Enter any Upper or Lower case English letter of the Alphabet."
        continue
    print"\n"
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
    print"\n"
