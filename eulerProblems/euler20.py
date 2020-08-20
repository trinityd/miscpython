import math

fact = math.factorial(100)
factstr = str(fact)

sum = 0
for i in range(len(factstr)):
    sum += int(factstr[i])

print(sum)