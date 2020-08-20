def isPrime(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

sum = 0

for i in range(0, 2000000):
    if isPrime(i): sum += i

print(sum)