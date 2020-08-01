#PA2 - 03 - Armstrong Numbers

def getText():
    try:
        my_file = open("FileIn.txt","r")
        numbers = map(int,((my_file.read()).split()))
        my_file.close()
    except ValueError:
        print "Invalid Input! Input file must contain integers!"
    except IOError:
        print "File Error!"
    else:
        if len(numbers)==2:
            if numbers[0]<numbers[1]:
                if 0<numbers[0]<1000 and numbers[1]<10000:
                    return numbers
                else:
                    print "Invalid Input! Input file must contain integers which are less than 10000 where first integer is less than 1000."
            else:
                print "Invalid Input! Input file must contain integers in the order of first integer < second integer."
        else:
            print "Invalid Input! Input file must contain only 2 integers values."

def showArmstrongNumbers(x):
    Armstrong = []
    Output = "M and N: %d %d"%(x[0],x[1])
    for i in range(x[0],x[1]+1):
        Sum = 0
        for j in str(i):
            Sum+=int(j)**len(str(i))
        if Sum==i:
            Armstrong.append(i)
    Output += "\nArmstrong numbers between M and N: "
    for i in Armstrong:
        Output+=str(i)+" "
    print Output
    try:
        myfile_2 = open("Result.txt","w")
        myfile_2.write(Output)
        myfile_2.close()
    except IOError:
        print "File Error!"

run = getText()
if run!=None:
    showArmstrongNumbers(run)
    
            
            
