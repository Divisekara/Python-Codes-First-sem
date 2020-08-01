n=int(raw_input("Enter n(height of the traingle):"))

num=[]
s_line=[]

for i in range(1,n+1):
    num=[]
    s_line=[]
    if i<10:
        for j in range(n-i):
            s_line.append("    ")
        
        for k in range(i,0,-1):
            num.append(k)
        
        line="".join(map(str,s_line)) + "   ".join(map(str,num))+"   " + "   ".join(map(str,num[-2::-1]))
        if i==1:
            line="".join(map(str,s_line)) + "1"
            
        print line
    else:
        for j in range(n-i):
            s_line.append("    ")
    
        for k in range(i,0,-1):
            num.append(k)
        line= "".join(map(str,s_line)) + "  ".join(map(str,num[0:n-10])) + "  " +  "   ".join(map(str,num[n-10:]))+"   " + "   ".join(map(str,num[-2::-1]))
        
        print line
            
