#PA1 - 8 - Minimum Maximum Exchanger

def swap(x_list,x,y):
	ix = x_list.index(x)
	iy = x_list.index(y)
	x_list[iy] = x
	x_list[ix] = y
a=1
while (a):
    try:
        t_list = raw_input("Enter a list of at least 7 positive integers (and less than 50) keeping spaces in between elements: ")
        m_list = []
        q = t_list.split()
        for i in q:
            if int(i)==-1:
                break
            else:
                m_list.append(int(i))
    except ValueError:
        print "Invalid Input! Enter numerical integers values for inputs."
        continue
    else:
        n = len(m_list)
        if n<6 or n>50:
            print "Invalid Input! List is not within required range. Input sequence of numbers inbetween 7 and 50."
            continue
        else:
            Max_list =[]
            Min_list =[]
            Final_list = []
            Final_list.extend(m_list)
            for x in range(3):
                Max = m_list[0] 
                for i in range(len(m_list)-1):
                    if x==1:
                        if i==m_list.index(Max_list[x-1])-1:
                            continue
                    elif x==2:
                        if i==m_list.index(Max_list[x-1])-1 or i==m_list.index(Max_list[x-2])-1:
                            continue
                    if Max<m_list[i+1]:
                        Max=m_list[i+1]
                Max_list.append(Max)
                Min = Max
                for i in range(len(m_list)-1):
                    if x==1:
                        if i==m_list.index(Min_list[x-1]):
                            continue
                    elif x==2:
                        if i==m_list.index(Min_list[x-1]) or i==m_list.index(Min_list[x-2]):
                            continue
                    if m_list[i]<Min:
                        Min=m_list[i]
                Min_list.append(Min)
                swap(Final_list,Min,Max)
            print "Output:"," ".join(map(str,Final_list)),"\n"
            
