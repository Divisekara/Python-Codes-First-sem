L=[[1,2,3],[23,45,[18,43,[12,876,[76,90,[56,34]]]]],[1,6,[23,78]]]



def flatten(L):
    if L==[]:
        return L
    if isinstance(L[0],list):
        return flatten(L[0]) + flatten(L[1:])
    return L[:1]+flatten(L[1:])


print flatten(L)






