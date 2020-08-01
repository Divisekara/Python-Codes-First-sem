def HCF(x,y):
    while y:
        x,y=y,x%y
    return x
print(reduce(lambda x,y:(x*y)//HCF(x,y) ,list(range(1,21))))
