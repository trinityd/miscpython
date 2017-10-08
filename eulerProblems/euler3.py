def isPrime(n):
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


n = 600851475143
mult = 1;
larg = 1;

for i in range(n):
    # print(f"Mult: {mult} Larg: {larg}\n")
    if mult != 1 and n == mult:
        break
    if isPrime(i) and n % i == 0:
        mult *= i
        larg = i

print(larg)
