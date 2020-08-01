#PA2 - 11 - Smallest Positive Integer

def getText():
    try:
        my_file = open("FileIn.txt","r")
        inputs = my_file.read()
        my_file.close()
        tempry_list = inputs.split()
        N = int(tempry_list.pop(0))
        input_list = map(int,tempry_list)
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input! Input lines should contain only integers!"
    else:
        if N>20 or N<0:
            print "Invalid Input! The first line should contain a positive integer less than or equal to 20."
        elif len(input_list)%10==0:
            candles_list=[]
            for i in range(len(input_list)/10):
                temp_list = []
                for k in range(10):
                    if 0<=int(input_list[0])<=6:
                        temp_list.append(input_list.pop(0))
                    else:
                        print "Invalid Input! Each integer in a line after first line onwards must be an integer less than 7."
                        break
                candles_list.append(temp_list)
            if N == len(candles_list):
                return candles_list
            else:
                print "Invalid Input! Input file must contain %d lines, each containing 10 integers."%N

def Show(x):
    smallest_int=[]
    integers=""
    for i in x:
        m=1
        j=0
        if i[0]==0:
            smallest_int.append(10)
            continue
        while m>0:
            for k in range(1,10):
                if i[k]==j:
                    smallest_int.append(int(str(k)*(j+1)))
                    m-=1
                    break
            j+=1
    for j in smallest_int:
        integers+=str(j)+"\n"
    print integers
    try:
        my_file_2 = open("Result.txt","w")
        my_file_2.write(integers)
        my_file_2.close()
    except IOError:
        print "File Error!"
    
my_data = getText()
if my_data!=None:
    Show(my_data)

