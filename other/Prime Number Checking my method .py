#for a in range(100):
while True:
    
    x=int(raw_input("Enter a number "))
    n=2
    for r in range (2,int(x**0.5)+1):
        if x%r==0:
            print x,"is not a prime."
            break
        n+=1
        if n==int(x**0.5)+1:
            print x,"is a prime"
            
