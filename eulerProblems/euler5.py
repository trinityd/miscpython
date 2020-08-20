def findn():
    n = 2540
    while True:
        for i in range(11,21):
            if n % i != 0: break
            if i == 19: return n

        n+=20
        print(n)

print(findn())