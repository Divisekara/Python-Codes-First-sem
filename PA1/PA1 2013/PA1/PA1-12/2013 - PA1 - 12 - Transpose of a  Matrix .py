#PA1 - 12 - Transpose of a Square Matrix

while True:
        try:
                N = int(raw_input("Enter N (where 1<N<10 for size NxN square matrix) = "))
                print "Enter the matrix row by row, seperating the elements with spaces."
                matrix = []
                if N>=10 or N<2:
                        print "Invalid Input! Enter N in correct range."
                n = 1
                for x in range(N):
                        while True:
                                row = map(int,raw_input("Enter row %d:"%n).split())
                                if len(row)!=N:
                                        print "Enter correct number of elements for row, seperating with spaces."
                                else:
                                        matrix.append(row)
                                        n+=1
                                        break
        except ValueError:
                print "Enter integer values for the row and column"
                continue
        else:
                transpose = ""
                for x in range(N):
                        for y in range(N):
                                transpose+=str(matrix[y][x])+" "
                        transpose+="\n"
                print "Transpose of the input matrix is = \n",transpose
                break
