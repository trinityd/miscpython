nums = [1, 6, 3, 9, 2, 5]

def min(numArr):
    curMin = float('inf')
    for num in nums:
        if num < curMin:
            curMin = num
    return curMin

def nthOrderStatistic(numArr, n):
    for i in range(n):
        numArr.remove(min(numArr))
    return min(numArr)

print(nthOrderStatistic(nums, 3))
