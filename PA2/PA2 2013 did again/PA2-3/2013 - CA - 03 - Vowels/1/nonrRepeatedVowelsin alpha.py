def getText():
    try:
        fileOpen=open("FileIn.txt","r")
        text=fileOpen.read()
        fileOpen.close()
        return text
    except:
        print "File Error!"

def show(text):
    List=text.split()
    output=''
    for word in List:
        letterList=list(word)
        vowelsInWord=[]
        for letter in letterList:
            if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
                vowelsInWord.append(letter)
        
        if len(vowelsInWord)==len(set(vowelsInWord)) and len(vowelsInWord)!=0:
            for i in range(len(vowelsInWord)-1):
                if not ord(vowelsInWord[i])<ord(vowelsInWord[i+1]):
                    break
            else:
                output+=word+"\n"
    print output
    return output
                
def saveFile(output):
    try:
        fileOpen=open("result.txt","w")
        fileOpen.write(output)
        fileOpen.close()
    except:
        print "File error!"
            

    
Text=getText()           
if Text!=None:
    saveFile(show(Text))
    
else:
    print "ERROR!"
