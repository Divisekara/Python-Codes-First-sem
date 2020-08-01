def selection_sort(L):
    for i in range(0,len(L)-1):
        min_index=i
        for j in range(i+1,len(L)):
            if L[j]<L[min_index]:
                min_index=j
        if min_index!=i:
            L[i],L[min_index]=L[min_index],L[i]
    return L

L=[5,3,7,2,9,1,0,4]
M=["j","b","r","a"]

print selection_sort(L)
print selection_sort(M)
            
