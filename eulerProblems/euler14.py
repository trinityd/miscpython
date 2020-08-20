import sys

def chainLength(n):
    length = 0
    while n != 1:
        if(n % 2 == 0): n /= 2
        else: n = (3 * n) + 1
        length += 1
    return length+1

longestLength = -sys.maxsize
num = 1
for i in range(1, 10**6):
    print(i)
    len = chainLength(i)
    if(len > longestLength):
        longestLength = len
        num = i


print(num)