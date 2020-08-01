def palin(x):
    y=x[::-1]
    if y==x and y.isalpha()==True and len(y)>1:
        return True
    else:
        return False

while True:
    word=raw_input("Enter word: ").strip()

    if word.isalpha()==False:
        print "Enter letters only\n"
        continue

    if word=="Bye" or word=="bye":
        print "Bye!\n"
        break
    
    L=[]
    if palin(word)==True:
        L.append(word) 

    else:
        for i in range(0,len(word)):
            for j in range(i,len(word)):
                x=word[i:j]
                if palin(x)==True:
                    L.append(x)
    print L
    if len(L)==0:
        print "There are no palindromes\n"
    else:
        length=max(map(len,L))
        for k in L:
            if len(k)==length:
                print "Lonogest Palindrome:",k,"\n"
                break
    

        
