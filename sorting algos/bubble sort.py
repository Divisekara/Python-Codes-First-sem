def bubble_sort(L):
    for i in range(0,len(L)-1):
        for j in range(0,len(L)-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    return L


L=[3,12345,2,8,123,4,12,  1]
M=["c","s","r","e","g","a"]
print bubble_sort(L)
print bubble_sort(M)
