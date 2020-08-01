#error handling
try:
    a=100
    b=int(raw_input("Entera a number"))
    print a/b
    
except ZeroDivisionError:
    print "Cant be divided by zero"
