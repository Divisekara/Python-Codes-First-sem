"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""



ans=0
for a in range(100,1000):
    for b in range(100,1000):
        x=a*b
        
        y=str(x)
        L=[]
        
        for i in(y):
            L.append(i)
            
        M=[]

        for j in(L):
            M.append(j)

        M.reverse()
        
        if L==M:
            if x>ans:
                ans = x
                print ans,'=',a,'x',b
            




"""
max([(i*y, i, y) for i in range(100,1000) for y in range(100,1000) if str(i*y) == str(i*y)[::-1]])
"""






"""
def palCheck(n):
        if (str(n) == str(n) [::-1]): return True #Very crafty way to check palindrome, saw it on Stack Overflow haha
        else: return False


palinList = []
for i in range(999, 99, -1):
        for j in range(999, 99, -1):
                if palCheck(i * j) == True:
                        palinList.append(i * j)
                else: continue

print(str(max(palinList)))
"""





"""
final = 0

def palindrome(num):
    return str(num) == str(num)[::-1]


palList = []
multipe =[]
for i in range(100,1000):
    first = i
    for x in range (100,1000):
        second = x
        final = (first * second)
        #print str("First " +str(first) + " * Second " +str(second)+ " = "+str(final))
        if palindrome(final):
            multipe.append(str(first) + " " + str(second))
            palList.append(final)
            multipe.sort(reverse =True)
            palList.sort(reverse=True)

print "Done! The figure was: " +  str(multipe[0])
print str(palList[0])
"""





"""
def is_palindrome(i):
    return i if str(i) == str(i)[::-1] else 0

my_max = 0
for x in range(999, 99, -1):
    if x ** 2 < my_max:
   	    break

    for y in range(x, 99, -1):
        my_max = max(my_max, is_palindrome(x * y))
print(my_max)
"""






"""
my solution, in python
max = 999
min = 100
i = 999;
j = 999;
k = 0;
reverse = "";
largest = "0";
done = False;

while not done: 
    if j < min:
        j = max
        i = i - 1
    k = str(i * j)
    reverse = k[::-1]	
    if k == reverse:
        if int(largest) > int(k):
            done = True
        else:
            largest = k
            i = i - 1
            j = max
    else:
        j = j - 1
print(largest)
"""







"""
largest = 0

for i in range(100,1000):
    for y in range(100,1000):
        string = str(i * y)
        palindrome = True
        for z in range(0, len(string) / 2):
            if string[z] != string[-z - 1]:
                palindrome = False
                break
        if i * y > largest and palindrome == True:
            largest = i * y

print("The largest palindrome is " + str(largest) + ".")
"""



"""
number1 = 100
number2 = 100
max_number = 999

largest = 0
countdown = 999
temp = 0
loop = True

def is_palindromic(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

while loop == True:
    temp = number1 * number2
    if is_palindromic(temp):
        if largest < temp:
            largest = temp
    number1 += 1
    countdown -= 1
    if countdown == 0 or number1 >= max_number:
        countdown = 999
        number1 = number2 + 1
        number2 += 1
    if number2 >= max_number:
        loop = False

print(largest)
"""







"""
enBuyuk = 0

for i in range(100,999):
    for j in range(100,999):
        carpim = i*j
        if  str(carpim) == str(carpim)[::-1]:
            if carpim > enBuyuk:
                enBuyuk = carpim
print("En Büyük Palindrom Sayı =", enBuyuk)
"""






"""
#Solution 1
p=[]
for x1 in range(9,0,-1):
    for y1 in range(9,0,-1):
        for x2 in range(9,-1,-1):
            for y2 in range(9,-1,-1):
                        for x3 in range(9,-1,-1):
                            for y3 in range(9,-1,-1):
                                z=str((100*x1+10*x2+x3)*(100*y1+10*y2+y3))
                                if z==z[::-1]:
                                    p.append(z)
p[0]
#Solution 2
l = []
for x in range(100,1000):
    for y in range(100,1000):
        z = str(x * y)
        if z == z[::-1]:
            l.append(z)
print(max(l))
"""
