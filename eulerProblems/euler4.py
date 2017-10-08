def isPal(n):
    strN = str(n)
    for i in range(int(len(strN) / 2)):
        # print(f"{strN[i]} comp to {strN[len(strN)-i-1]} ", end='')
        if strN[i] != strN[len(strN)-i-1]: return False
    return True

n = 997799
f = 0;

for i in range(n,0,-1):
    if f == 1: break
    if isPal(i):
        for j in range(999,100,-1):
            if f == 1: break
            if i % j == 0:
                for k in range(999, 100, -1):
                    if i == j*k:
                        print(f"Num: {i} Mults: {j} and {k}")
                        f = 1
