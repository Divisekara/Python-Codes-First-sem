#PA2 - 15 - Derivative Sequence of Order N

def getText():                                              #To define a fucntion for obataining input.
    #To red the input file
    try:
        fileOpen = open("FileIn.txt","r")                   #To create a file object by openeing the .txt file containing the string for reading only.
        nums = (fileOpen.read()).split("\n")                #To read the string in the .txt file and assign it to variable.
        fileOpen.close()                                    #To close the opened file object.
        if len(nums)==0:
            print "File Empty!"
        elif len(nums)>=2:
            N=int(nums[-1])                                 #Take the final element of the input file as N
            nums2=nums[0].split()
            nums2=map(int,nums2)
    except IOError:                                         #To handle any errors in case there is no .txt file.
        print "File Error!" 
    except ValueError:                                      #To handle any errors if the FileIn.txt contains any non-integer objects.
        print "Invalid Input! All inputs must be integer values."
    else:
        if len(nums)>=2:
            if 1<=(len(nums2))<=100:
                if N<len(nums2):
                    nums2.append(N)
                    return nums2                            #Return the list only if conditions are satisfied.
                else:
                    print "Invalid Input! The integer on last line must be less than the length of the input sequence."
            else:
                print "Invalid Input! Length of input sequence must be greater than 1 and less than 100."
        else:
            print "Invalid Input! Integer N not in Input file."

def derivative(x):
    #To find the derivative sequence of order N.
    N=x.pop(-1)
    for i in range(N):
        if i==0:                                            #To start the process with the given Input sequence A
            deri=x[:]
        for j in range(len(deri)-1):
            if j==0:
                deri2=[]                                    #To append into the new list, the differences, so make it empty at the start.
            num1 = deri[j]
            num2 = deri[j+1]
            diff = num2-num1                                #To get the difference between adjacent terms and append to another list.
            deri2.append(diff)
        deri=[]                                             #To make the original list empty.
        deri.extend(deri2)                                  #To make the original list the difference sequence.
    output = " ".join(map(str,deri))
    return output                                           #To return the output

def showResult(output):                                     #To define a function for saving 
    #To print the output on screen and to the output file.
    print output
    try:
        fileOut = open("result.txt","w")                    #To create a file object by opening the .txt file for writing only.
        fileOut.write(output)                               #To write a string in the .txt file 
        fileOut.close()                                     #To close the opened file object
    except IOError:                                         #To handle any errors in case there is no .txt file
        print "File Error!"

run = getText()                                             #To call the functions in a global level
if run!=None:                                               
    showResult(derivative(run))
else:
    print "Please recheck your Input file!"
