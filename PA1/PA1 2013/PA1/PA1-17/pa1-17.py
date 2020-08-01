while True:
    try:
        n=raw_input("Enter the x coordinates and y coordinates respectively by seperated spaces:").split()
        coordinates=[]
        for i in n:
            coordinates.append(int(i))

    except ValueError:
        print "Enter numerical values only."

    except:
        print "Something went wrong. Try again with a difference input."

    else:
        p1=[coordinates[0],coordinates[4]]
        p2=[coordinates[1],coordinates[5]]
        p3=[coordinates[2],coordinates[6]]
        p4=[coordinates[3],coordinates[7]]

        a= p1[1] - p2[1] 
        b= p2[0] - p1[0]
        c= p2[1]*b*(-1) - p2[0]*a

        num_p3=a*p3[0]+b*p3[1]+c
        num_p4=a*p4[0]+b*p4[1]+c
        
        if (num_p3>0 and num_p4>0):
            print "p3 and p4 are on same side."
        elif (num_p3<0 and num_p4<0):
            print "p3 and p4 are on same side."
        elif (num_p3<0 and num_p4>0):
            print "p3 and p4 are on opposite side."
        elif (num_p3>0 and num_p4<0):
            print "p3 and p4 are on opposite side."
        else:
            print "p3 and p4 lie on the straight line"
