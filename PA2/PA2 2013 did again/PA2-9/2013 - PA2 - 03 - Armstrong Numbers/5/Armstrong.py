def getText():
    "a function to read a line of text from a file"
    global m
    global n
    global fo_out
    fo_in = open("FileIn.txt", "r")
    fo_out = open("result.txt", "w")
    str_m_n = fo_in.read()
    if len(str_m_n) > 10:
        fo_out.write("Invalid Input : String has exceeded the character limit")
        fo_out.close()
        print "Invalid Input"
    elif len(str_m_n) == 0:
        fo_out.write("Invalid Input : Empty Input")
        fo_out.close()
        print "Invalid Input : Empty Input"
    else:
        m_n_lst = str_m_n.split(" ")
        if len(m_n_lst) > 2 or len(m_n_lst) == 0:
            fo_out.write("Invalid Input : more than two numbers or extra spaces")
            fo_out.close()
            print "Invalid Input : more than two numbers or extra spaces"
        else:
            m = int(m_n_lst[0])
            n = int(m_n_lst[1])
            fo_in.close()
            if m > 999 or n > 9999 or m <= 0 or m > n:
                print "M or N not according to the arguements"
                fo_out.write("M or N not according to the arguements")
                fo_out.close()
            else:
                return True


def showArmstrongNumbers(x,y):
    global arm_num_lst
    arm_num_lst = []
    for i in range(x,y+1):
        p = len(str(i))
        arm_check = 0
        for j in str(i):
            arm_check += int(j)**p
        else:
            if arm_check == i:
                arm_num_lst.append(str(i))
            else:
                continue
    else:
        fo_out.write("M and N: "+str(m)+" "+str(n))
        print "M and N: ",m,n
        if len(arm_num_lst) == 0:
            print "Armstrongstrong Number between M and N: No ArmStrong Numbers in that range",
            fo_out.write("\nArmstrongstrong Number between M and N: No ArmStrong Numbers in that range")
            fo_out.close()
        else:
            print "Armstrongstrong Number between M and N: "," ".join(arm_num_lst)
            fo_out.write("\nArmstrongstrong Number between M and N: "+" ".join(arm_num_lst))
            fo_out.close()
    return



if getText():
    showArmstrongNumbers(m,n)
        
        
        
