def getInput():
    'a function to get inputs from a text file'
    try:
        fo_in = open("FileIn.txt", "r")

        global N
        N = int(fo_in.readline())                                   #reading the order of the square matrix
        ''' when storing the matix in the list
            a set of zeroes sorrounding the matrix
            are added by the program.
            this will cover the entire original matrix with
            0s. This is done for the use in the program '''
            
        global mat_A                                                #making an empty list to store the matrix
        mat_A = [[0]*(N+2)]                                   
        
        for i in range(5):
            mat_A_row = fo_in.readline().split(" ")
            mat_A_row_int = [0]
            for j in mat_A_row:
                mat_A_row_int.append(int(j))
            else:
                mat_A_row_int.append(0)
                mat_A.append(mat_A_row_int)
                
        else:
            mat_A.append([0]*(N+2))
            return True

    except IOError:
        print "No file in the Directory"
    except ValueError:
        print "Invalid Entries"

def show():
    global mat_B
    mat_B = []
    '''when adding the elements around an element on the edge of the matrix index errors occur. to overcome this the 0s were added when creating the matrix.
        this way the zeroes are added instead of getting errors. and whenever a zero is added the number to be divided by when avearaging is reduced by one.'''
    for i in range(1,N+1):
        mat_B_row = []
        for j in range(1,N+1):
            count = 9
            B_i_j = 0
            for h in [-1,0,1]:
                for g in [-1,0,1]:
                        B_i_j += mat_A[i+g][j+h]
                        if i+g == 0 or i+g == 6 or j+h == 0 or j+h == 6:
                            count -= 1
            else:
                mat_B_row.append(B_i_j/count)
        else:
            mat_B.append(mat_B_row)
    else:
        global mat_B_t
        mat_B_t =[]
        for i in mat_B:
            mat_B_t_r = []
            for g in i:
                mat_B_t_r.append(str(g))
            else:
                mat_B_t.append(mat_B_t_r)
        else:
            for i in mat_B_t:
                print ' '.join(i)
        
def saveFile():
    fo_out = open("result.txt" , "w")
    for i in mat_B_t:
        fo_out.write(' '.join(i))
        fo_out.write("\n")
    else:
        fo_out.close()
    


        

if getInput():
    show()
    saveFile()
   
    
