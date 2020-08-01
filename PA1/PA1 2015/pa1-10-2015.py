def vowel_remove(word):
    L=list(word)
    vowel=""
    for i in L:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            vowel += L.pop(L.index(i))

    return "".join(L),vowel

while True:
    s=raw_input().strip().split()

    raw="".join(s)
    
    if raw.isalpha()==False:
        print "Enter letters only."
        continue

    print "Disemvoweled: %s \nVowels: %s" %(vowel_remove(raw)[0],vowel_remove(raw)[1])
