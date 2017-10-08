i1 = 1
i2 = 2
save1 = 0;
save2 = 0;
sum = 0;

# print(str(i1) + " " + str(i2) + " ", end='')
print(f"{i1} {i2} ", end='')
while True:
    if i2 > 4e6:
        break
    # print(str(i2) + " ", end='')
    if i2 % 2 == 0:
        sum += i2
    save1 = i1
    save2 = i2
    i1 = i2
    i2 = save1 + save2
    print(f"{i2} ", end='')

print(f"\ni2 = {i1} Sum = {sum}")