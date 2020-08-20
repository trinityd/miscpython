amt = int(input("Amount of fibonacci numbers you would like printed: "))

last = 0
cur = 1
for i in range(0, amt):
    print(cur, end=" ")
    save = cur
    cur += last
    last = save