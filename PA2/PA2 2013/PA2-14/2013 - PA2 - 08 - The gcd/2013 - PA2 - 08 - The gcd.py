#PA2 - 08 - The GCD

def getText():
    try:
        my_file = open("FileIn.txt","r")
        numbers = my_file.read().split()
        my_file.close()
        num_list = map(int,numbers)
        N = int(num_list.pop(0))
    except IOError:
        print "File Error!"
    except ValueError:
        print "Invalid Input! Input file must contain only integers!"
    else:
        if N>20 or N<0:
            print "Invalid Input! First line must contain an integer less than or equal to 20."
        else:
            int_list = []
            for i in range(N):
                temp_list=[]
                for j in range(3):
                    if 0<=num_list[0]<=1000:
                        temp_list.append(num_list.pop(0))
                    else:
                        print "Invalid Input! Each positive integer must be less than 1000."
                        break
                int_list.append(temp_list)
            if N==len(int_list):
                for i in int_list:
                    if len(i)!=3:
                        print "Invalid Input! Each line must contain only 3 positive integer values."
                    else:
                        return int_list
            else:
                print "Invalid Input! Input file must contain %N lines excluding the first line"%N

def int_gcd(a,b):
    if b==0:
        return a
    else:
        return int_gcd(b,a%b)

def int_gcd_extend(a,b,c):
    if c==0:
        return int_gcd(a,b)
    else:
        return int_gcd(c,int_gcd(a,b)%c)
    
def gcd(x):
    gcd_list=[]
    for i in x:
        gcd_list.append(int_gcd_extend(i[0],i[1],i[2]))
    return gcd_list
    
def saveFile(x,y,z):
    final = ""
    for i in range(x):
        final += "gcd (%s) = %d"%(" ,".join(map(str,y[i])),z[i])+"\n\n"
    print final
    try:
        my_file_2 = open("Result.txt","w")
        my_file_2.write(final)
        my_file_2.close()
    except IOError:
        print "File Error!"

List = getText()
if List!=None:
    saveFile(len(List),List,gcd(List))
