import math

oneToNine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tenToNineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
twentyToNinety = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"

def numToWord(num):
    if (num == 1000): return "onethousand"
    word = ""
    hundredsPlace = math.floor(num / 100) % 10
    tensPlace = math.floor(num / 10) % 10
    onesPlace = math.floor(num / 1) % 10

    if(hundredsPlace != 0):
        word += oneToNine[hundredsPlace-1] + hundred
        if(num % 100 != 0): word += "and"
    if(tensPlace != 0):
        if(tensPlace == 1):
            word += tenToNineteen[onesPlace]
        else:
            word += twentyToNinety[tensPlace - 2]
    if(tensPlace != 1 and onesPlace != 0):
        word += oneToNine[onesPlace-1]

    return word

n = 10
print(numToWord(n), len(numToWord(n)))

sum = 0
for i in range(1, 1001):
    print(i)
    sum += len(numToWord(i))

print(sum)