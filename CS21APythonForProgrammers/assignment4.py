# Defines spell, a function which takes a whole number as input and returns that number as a string in English words. Prints some hardcoded numbers using spell.

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen"]
tens = ["", "ten ", "twenty ", "thirty ", "fourty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
digitTerms = ['hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion ', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']

# Returns num less than 10 in English
# No reading from shell
# No writing to shell
def spellLessThan10(num):
    return ones[num]

# Returns num less than 1000 in English
# No reading from shell
# No writing to shell
def spellThreeDigitNumber(num):
    wordsStr = ""
    if num != 0:
        if num >= 100: wordsStr += spellLessThan10(int(num/100)) + " hundred "
        remainder = num % 100
        if remainder == 0:
            return wordsStr

        if remainder >= 10 and remainder <= 19:
            return wordsStr + teens[int(remainder % 10)] + " "

        wordsStr += tens[int(remainder/10)]
        remainder = num % 10
        if remainder == 0:
            return wordsStr
        
        wordsStr += spellLessThan10(remainder) + " "

    return wordsStr

# Returns num in range -999999999-999999999 in English
# No reading from shell
# Yes writing to shell
def spell(num):
    wordsStr = ""
    if num < 0:
        wordsStr += "negative "
        num = abs(num)
    if num < 10:
        wordsStr += spellLessThan10(num)
    elif num == 10:
        wordsStr += "ten"
    elif num < 1000:
        wordsStr += spellThreeDigitNumber(num)
    else:
        remainder = num
        pows = round(len(str(num))/3)
        for i in reversed(range(pows)):
            section = int(remainder/pow(1000, i))
            wordsStr += spellThreeDigitNumber(section) + (digitTerms[i] if i > 0 else "") + " "
            remainder = remainder % pow(1000, i)

    return wordsStr

print (spell (123456789) )  
print (spell (456678) )   
print (spell (66) )       
print (spell (-123456789) )
print (spell (-456678) )      
print (spell (-418) )      
print (spell (-13456678) )
print (spell (0) )
print (spell (10004) )

print (spell (-999999999 ) )
print (spell (999999999 ) )

""" A RECORDING OF THE RUN
one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
four hundred fifty six thousand six hundred seventy eight
sixty six
negative one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
negative four hundred fifty six thousand six hundred seventy eight
negative four hundred eightteen
negative thirteen million four hundred fifty six thousand six hundred seventy eight
zero
ten thousand four
negative nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine
nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine
"""