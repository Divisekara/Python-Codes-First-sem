def gcd(a, b):
    #Return greatest common divisor using Euclids Algorithm.
    while b:      
        a, b = b, a % b
    return a

print gcd(12,13)
