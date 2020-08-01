sen1=list("".join(raw_input("enter first sentence: ").lower().split()))
sen2=list("".join(raw_input("enter secnd sentence: ").lower().split()))

a=1

for i in sen1:
    if not sen1.count(i)==sen2.count(i):
        a=-1
        break
else:
    for j in sen2:
        if not sen2.count(i)==sen1.count(i):
            a=-1
            break
if a==1:
    print "These are anagrams"
else:
    print "These are not anagrams"














"""
Eleven plus two
Twelve plus one

Eleven plus four
Fourteen plus one
"""
