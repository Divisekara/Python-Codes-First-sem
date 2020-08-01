while True:
    try:    
        x=raw_input("Enter the input word: ").lower()

    except ValueError:
        print "Invalid input."
        continue

    else:
        if x.isalpha()==False:
            print "Invalid Input."
            continue
            
        word=[]
        for i in range(0,len(x)):
            if x[0:i]==x[-i:]:
                word+=[len(x[0:i])]
        print max(word)
        
    finally:
        print "\n"

    
