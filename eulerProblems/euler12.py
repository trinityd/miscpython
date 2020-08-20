def isPrime(n):
    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

primes = []
for i in range(1000):
    if(isPrime(i)): primes.append(i)

def decompose(n):
    ret = []
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            ret.append(p)
            n //=p
    if n > 1:
        ret.append(n)
    return ret

def numDivisors(n):
    dec = decompose(n)
    print(dec)
    num = 1
    checked = []
    for prime in dec:
        if prime not in checked:
            num *= dec.count(prime)+1
            checked.append(prime)
    return num

def findTri(amt):
    i = 0
    triNum = 0
    while True:
        i += 1
        if (isPrime(i) and i not in primes): primes.append(i)
        triNum += i
        numDivisors_ = numDivisors(triNum)
        if(numDivisors_ > amt):
            return triNum
        #print(f"Trinum: {triNum} NumDiv: {numDivisors_}")

print(findTri(500))