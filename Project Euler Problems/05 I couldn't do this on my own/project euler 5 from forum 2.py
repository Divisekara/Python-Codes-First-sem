def gcd(a, b):
    #Return greatest common divisor using Euclids Algorithm.
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    #Return lowest common multiple.
    return a * b // gcd(a, b)

def lcmm(*args):
    #Return lcm of args.
    return reduce(lcm, args)
