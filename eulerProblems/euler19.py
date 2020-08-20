def getDaysInMonth(month, year):
    if(month == 1 and (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0))): return 29
    switcher = {
        0: 31,
        1: 28,
        2: 31,
        3: 30,
        4: 31,
        5: 30,
        6: 31,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31
    }
    return switcher.get(month)

year = 1901
month = 0
dayOfWeek = 0

numSundays = 0
prevNS = 0

endYear = 2000
endMonth = 11
endDay = 30
endFlag = False

while True:
    daysInMonth = getDaysInMonth(month, year)
    for day in range(daysInMonth):
        if (day == 0 and dayOfWeek == 6): numSundays += 1
        dayOfWeek = (dayOfWeek + 1) % 7

        if (year == endYear and month == endMonth and day == endDay):
            endFlag = True
            break

    # print(f"Month: {month} DIM: {daysInMonth} Year: {year} NumSun: {numSundays - prevNS} TotNumSum: {numSundays}")
    prevNS = numSundays
    if (endFlag): break
    month = (month + 1) % 12
    if(month == 0): year += 1

print(numSundays)