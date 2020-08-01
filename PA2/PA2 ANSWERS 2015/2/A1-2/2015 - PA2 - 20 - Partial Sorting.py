#PA2 -  20 - Partial Sorting

def getText():
    #To get text from input and check for any errors.
    try:
        fileOpen=open("FileIn.txt","r")                                                         
        numbers=fileOpen.read().split()
        fileOpen.close()
        pivot_n = int(numbers.pop(0))
        numbers=map(int,numbers)
    except ValueError:
        print "Invalid Input!"
    except IOError:
        print "File Error!"
    else:
        pivot = numbers[pivot_n]
        if 0<len(numbers)<100:
            if 0<=pivot_n<=len(numbers)-1:
                numbers.append(pivot_n)
                return numbers
            else:
                print "Invalid Input!"
        else:
            print "Invalid Input!"

def partial_sort(x):
    #To partially sort the list.
    pivot_n=x.pop()
    pivot=x.pop(pivot_n)
    my_list=[]
    my_list.append(pivot)
    for i in range(len(x)):
        if x[i]<pivot:
            my_list.insert(my_list.index(pivot),x[i])
        else:
            my_list.insert(len(my_list)+1,x[i])
    output=" ".join(map(str,my_list))
    return output

def show(output):
    #To print the output on screen as well as write to a file.
    print output
    try:
        fileWrite=open("Result.txt","w")                                                        
        fileWrite.write(output)
        fileWrite.close()
    except IOError:
        print "File Error!"

run = getText()   #To call functions in a global level                                                                                  
if run!=None:
    show(partial_sort(run))                                                                            


