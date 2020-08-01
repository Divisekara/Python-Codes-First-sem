def lcm(a, b):
    #Return lowest common multiple.
    return a * b // gcd(a, b) #gcd stands for greatest common factor
print lcm(12,10)
