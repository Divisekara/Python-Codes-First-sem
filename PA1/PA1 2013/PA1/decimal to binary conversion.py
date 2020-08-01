def decimal_to_binary(decimal):
    binary = ""
    while decimal>0:
        binary += str(decimal%2)
        decimal /= 2
    binary = binary[::-1]
    return binary

print decimal_to_binary(8)

#bin(integer) is the buit in function
