def quicksort(A):
    quicksort2(A,0,len(A)-1)

def quicksort2(A,low,hi):
    if low<hi:
        p=partition(A,low,hi)
        quicksort2(A,low,p-1)
        quicksort2(A,p+1,hi)
        
def getpivot(A,low,hi):
    mid=(hi+low)//2
    pivot=hi
    if A[low]<A[mid]:
        if A[mid]<A[hi]:
            pivot=mid
    elif A[low]<A[hi]:
        pivot=low
    return pivot

def partition(A,low,hi):
    pivotIndex=getpivot(A,low,hi)
    pivotValue=A[pivotIndex]
    A[pivotIndex],A[low]=A[low],A[pivotIndex]
    border=low

    for i in range(low,hi+1):
        if A[i]<pivotValue:
            border+=1
            A[i],A[border]=A[border],A[i]
    A[low],A[border]=A[border],A[low]
    return border

A=[2,5,3,4,1,6,1,87,9,6,7,54,3,4,54,5,5676,77]
B=["i","f","j","w","a","c"]
quicksort(A) 
quicksort(B)
print A
print B
