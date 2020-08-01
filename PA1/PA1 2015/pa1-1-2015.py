try:
    n=raw_input("Enter the positive integer sequence by space seperated: ").split() # Taking the input number of sequence as a list.

    L=[]  #collecting the numbers which are power of two. 

    for i in n: #taking one by one numbers in input sequence which are still in string format.
        
        m=int(i) #converting string format integers into. INTEGER format.
        
        if not 0<=m: continue #If there is a negative number avoiding from that number.
        
        while m!=1:
            
            if m%2==0: m=m//2 #Checking whether number is divisible continously until it gets 1.
            
            else: break # once it is not divisible by two getting the number avoided.

            if m==1: L.append(int(i)) #if successfully number finally gets one it is appended into the predefined list.

        if int(i)==1: L.append(m) # if there is number one in the given input sequence it is appended into the list. Just because it is power of 0.

except ValueError: #if there is any other format except integers in the sequence. Taking the decission against sprung out error.
    print "Enter positive integers only."

except: #If there is an unrecognized error sprung out getting the program healed.
    print "Something went wrong. Try again with a difference."

else: #If there is no error occured giving the output.
    print "Number of powers of two: %s" %(len(L)) #printing the output.

finally:
    "\n"


"23 32 1 45 67 128 2048 1024 87 16"
    
