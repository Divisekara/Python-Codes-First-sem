def mergesort(L):
    if len(L)>1:
        mid=len(L)//2
        lefthalf=L[:mid]
        righthalf=L[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                L[k]=lefthalf[i]
                i+=1

            else:
                L[k]=righthalf[j]
                j+=1
            k+=1

        while i<len(lefthalf):
            L[k]=lefthalf[i]
            i+=1
            k+=1

        while j<len(righthalf):
            L[k]=righthalf[j]
            j+=1
            k+=1


L=[54,26,93,17,77,31,44,55,20]
mergesort(L)
print L
