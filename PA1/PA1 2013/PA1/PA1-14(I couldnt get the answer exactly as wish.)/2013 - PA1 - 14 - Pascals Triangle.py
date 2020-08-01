#PA1-14 - Pascal's Triangle

print "Welcome to the Pascal's Triangle Generator!\n"
line = ""
while True:
    try:
        n = int(raw_input("Enter an integer n: 0<n<50 (The height of the Pascal's triangle): "))
    except ValueError:
        print "Invalid Input! Input should be an integer value.\n"
        continue
    else:
        if n<0 or n>50:
            print "Invalid Input! Input should be and integer inbetween 0 and 50.\n"
            continue
        j = 0
        nline=""
        for x in range(n):
            sums=[]
            line=[]
            s_line=[]
            for y in range(n-x):
                s_line.append("    ")
            line.append("1")
            if x==1:
                line.append("1")
                m=["1","1"]
            if x!=0 and x!=1:
                for i in range(len(m)):
                    if i==len(m)-1:
                        break
                    j = int(m[i])+int(m[i+1])
                    sums.append(str(j))
                for k in range(len(m)-1): 
                    line.append(sums[k])
                line.append("1")
                m=[]
                m.extend(line)
            t_line = ""
            for a in line:
                t_line += "%8s"%a
            sline = "".join(s_line)
            nline+=sline+t_line+"\n"
        print nline

##def pascal(n):
##    if n == 1:
##        return [1]
##    else:
##        line = [1]
##        previous_line = pascal(n-1)
##        for i in range(len(previous_line)-1):
##            line.append(previous_line[i] + previous_line[i+1])
##        line += [1]
##    return line
##
##print(pascal(6))
