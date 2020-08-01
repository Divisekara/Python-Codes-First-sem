while True:

    a=float(input("Give the first number a="))
    b=float(input("Give the second number b="))

    print """
    Select an operation
    
    1.Addition(a+b)
    2.Substraction(a-b)
    3.Multiplication(axb)
    4.Division(a/b)
    5.Exit from these two numbers
    """

    while True:
        
        x=int(input("Select a number among 1,2,3,4,5:- "))

        if x==1:
            print "The answer is ", a+b
        elif x==2:
            print "The answer is ", a-b
        elif x==3:
            print "The answer is ", a*b
        elif x==4:
            print "The answer is ", a/b
        elif x==5:
            print "... ..Exiting......"
            break
        else:
            print """
            Invalid input. Give a valid number among 1,2,3,4
            """

        print "..............................................."
    print ".......\t.........\n.......\t........."
