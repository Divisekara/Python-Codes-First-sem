while True:
    n=int(raw_input("Give a number "))
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            print 'not a prime'
            break
            
    if is_prime==True:
        print n ,'is a prime' 

                
        
