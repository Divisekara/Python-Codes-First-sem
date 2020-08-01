a=0
A=[]
C=[]
def read(): # to take inputs
    global a #taking the global a
    global A #taking the global A
    try:
        filop=open('PA1.txt','r+') #openning the file
        strnn=filop.read() #reading the file
        strnn=map(int,strnn.split()) #getiing the splited list to convert to int
        strnn.sort()
        print strnn
        A=strnn #equagting the global list to the strnn  # YOU SHOULD CALL THE GLOBAL LIST TO DO THIS!
        if len(strnn)!=2: #for numbers more than 2 ranged
            print 'you have not entered two numbers'
            a=1
    except IOError: #to handle error for not having the file there
        print 'file is not there'
        a=1
    except ValueError: #for non integer range input
        print 'no integer input'
        a=1
    except: #for any other exception
        print 'Invalid Input'

def compute(): #To compute the number
    for x in range(A[0],A[1]+1): #taking from range of two given numbers
        lenn=len(str(x)) #taking the first number of out, in the range and getttin its length
        B=[] #having  a local list
        for y in str(x): #appending each of the number 
            B.append(int(y)) #appending it to local list B after conversion
        else:
            num=0 #defining the loacl variable
            for xx in B: # taking each digit of the number
                num+=xx**lenn #taking the lenght power of it and adding up for each digit
            else:
                if num==x: #if added up power equals to the nnumber
                    C.append(x) #then append it to the global list

def out():
    print 'M and N is: %d %d'%(A[0],A[1])
    print 'Armstrong numbers beween M and N: ',
    filop2=open('PA1out.txt','wb')
    filop2.write('Armstrong numbers between M and N: ') ##**
    filop2.write('\r\n') ##### WHY NOT WORKING????####
    for x in C: #takes the global list automatically
        print str(x), ##THIS STILL CONNECTS TO ##**
        filop2.write('%d \n'%(x))
        filop2.write('\n')
    
read()
if a==0:
    compute()
    print C
    out()
    

