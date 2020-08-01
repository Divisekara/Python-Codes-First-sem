a=list(raw_input("Enter input pharse: ")) #taking the input an getting it listed

answer="" #Defining the string wish to append the output step by step

for i in a: #taking character one by one
    if i.isalpha()==True: #checking whether the character is an alphabetical or any other
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u": #Checking whether the letter is a vowel 
            con=i # if it is a vowel doing nothing just giving the output with same.
        else: #if it is either letter nor a vowel doing the procedure.
            con="" #Defining a string wish to formatas want
            con=i+"o"+i.lower() #Formatting the combination
    else: #If it is not a letter then printing just it
        con=i

    answer += con #Collecting the combinations 
print answer #printing the output as wish




"""
Hohelollolo Wowororloldod!
Hohelollolo Wowororloldod!

b
bob

wowhoherore isos gogodod!
wowhoherore isos gogodod!
"""
