'''
while True:

    x=int(input("Input a number that want the addition of any amount of consecutive numbers:-"))
    y=int(input("How many numbers do you want to add which are bigger than given number and consecutive for it:-"))
    sum_=x
    for i in range(1,y+1):
        x=x+1
        sum_=sum_+x

    print "Total of ",y+1, " consecutive numbers which are started from ",x-y , " is:-",sum_    
'''



while True:
    
    a=x=int(input("Input a starting number that want the addition of any amount of consecutive numbers:-"))
    y=int(input("Input a ending number that want the addition of any amount of consecutive numbers:-"))
    a=x
    sum_=x
    for i in range(1,y-x+1):
        x=x+1
        sum_=sum_+x

    print "Total of given consecutive numbers which are started from ",a," and ended from ",y ,"is :-",sum_
        

