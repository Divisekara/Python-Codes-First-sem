def binary(x): #integer input and output is the string of binary number
    b=list(bin(x))
    b=b[2:]
    return "".join(map(str,b))


def palin(x): #string input and output is True or False
    if x==x[::-1]:
        return "yes"
    else:
        return "No"
    
while True:
    try: 
        print "\n" , palin(binary(int(raw_input("Enter a number:")))) 
    except ValueError:
        continue
