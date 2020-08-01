#PA1 - 13 - Triangular Matrix

a = 1
while (a):
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
    
