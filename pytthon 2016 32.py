i=1
while (i<152):
    j=2
    while (j<=(i/j)):
        if not(i%j):
            break
        j+=1
    if j>i/j:print i
    i+=1

    
