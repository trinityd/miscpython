a = 1
b = 2
c = 3

for a in range(0, 1000):
    for b in range(0, 1000):
        for c in range(0, 1000):
            if(a < b and b < c and a**2 + b**2 == c**2 and a + b + c == 1000): print(a * b * c)
