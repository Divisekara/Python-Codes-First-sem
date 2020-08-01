letter=raw_input("Enter lowercase letter:")
i=ord(letter)-96

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for n in range(1,i+1):
    for x in range(i-n):
        print "",
    if n==1:
        print alphabet[n-1]
        continue
    print "%s%s"%(alphabet[:n],alphabet[n-2::-1])

for n in range(1,i):
    for x in range(n):
        print "",
    if n==i-1:
        print alphabet[i-n-1]
        continue
    print "%s%s"%(alphabet[:i-n],alphabet[i-n-2::-1])
print "\n"
