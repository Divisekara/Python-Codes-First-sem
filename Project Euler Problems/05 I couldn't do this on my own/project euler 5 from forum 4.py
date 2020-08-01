fin = 0
num = 2520
while fin == 0:
    fin = 1
    for i in range(1,21):
        if num%i != 0:
            fin = 0

    num = num+2520

print(str(num-2520))
