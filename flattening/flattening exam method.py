def FlattenList(mylist):
    retlist = []
    if len(mylist)==0:
        return []
    elif (type(mylist[0]) is list):
        retlist.extend(FlattenList(mylist[0]))
    else:
        retlist.append(mylist[0])
    retlist.extend(FlattenList(mylist[1:]))
    return retlist

l=[1,2,[2,3,4,5,[34,56,67,78],[12,23,23,32]]]
print FlattenList(l)
        
