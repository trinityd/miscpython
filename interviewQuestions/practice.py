# 1) Write code to check a String is palindrome or not? (solution)

# A palindrome is those String whose reverse is equal to the original. 

def isPalindrome(string):
    return string == string[::-1]

# print(isPalindrome("racecar"))

# 1.1) What is the difference between "is" and "!="?

# Former checks for if same object, latter checks for value equality. So:
# string is string[::-1]
# will always return false, but 
# return string == string[::-1]
# works as expected


# 2) Write a method which will remove all instances of any given substring from a String? (solution)

def removeChar(string, substr):
    return string.replace(substr, "")

s = "racecar"
s = removeChar(s, 'a')
# print(s)

# Note: ***STRINGS ARE IMMUTABLE! Stick to return and assign***


# 2.1) How about first instance?

def removeFirstInstChar(string, substr):
    return string.replace(substr, "", 1)

s = "racecar"
s = removeFirstInstChar(s, 'a')
# print(s)

# 3) Print all permutation of list both iterative and Recursive way? (solution)

# Using itertools
import itertools
# print(list(itertools.permutations([1,2,3])))

# Iterative
# General idea: build all size 1 perms (done if list/str is split into items). Build all size 2 perms by placing all unused items (in context of each size 1 perm) in front of each size 1 perm. Etc until size of original list is reached
# Bonus: can easily get perms of any size from this method, so put them in a dict for easy access

txt = list("0123")
perms = []

# Optional complexity: for input lists with duplicate items, e.g. '022', only add distinct permutations
onlyDistinct = False

def findPermsIteratively(original, outputList):
    permsInProgress = {
        "0": [],
        "1": original[:]
    }
    for i in range(2, len(original)+1):
        permsInProgress[str(i)] = []
        for perm in permsInProgress[str(i-1)]:
            for item in original:
                if item not in perm: permsInProgress[str(i)].append(item + perm[:])
                # print(permsInProgress)

    outputList.extend(permsInProgress[str(len(original))])
    outputList.sort()
            

findPermsIteratively(txt, perms)
# print(perms)
# for p in perms: print("".join(p))

# Recursive
txt = list("0123")
perms = []

# Optional complexity: for input lists with duplicate items, e.g. '022', only add distinct permutations
onlyDistinct = False

def findPermsRecursively(original, onlyAddDistinct=False, used=None, currentPerm=None, outputList=None):

    # Get around mutable default assignments. Dumb feature, wow.
    if used == None: used = [0 for i in range(len(original))]
    if currentPerm == None: currentPerm = []
    if outputList == None: outputList = perms
    # Base: permutation done! Add to output list (or don't, depending on distinct permutation setting)
    if len(currentPerm) == len(original):
        if not onlyAddDistinct or (onlyAddDistinct and currentPerm not in outputList):  
            outputList.append(currentPerm)
        return

    for j in range(len(original)):
        # If current item has not been used
        if used[j] == 0:
            # Mark it as used
            usedCopy = used[:]
            usedCopy[j] = 1
            # Call recursively with the original list, used item markers, and in progress permutation + the item we just marked as used
            findPermsRecursively(original, onlyAddDistinct, usedCopy, currentPerm + [original[j]], outputList)

findPermsRecursively(txt, onlyDistinct)
# for p in perms: print("".join(p))

# 4) Write a function to find out longest palindrome in a given string? (solution)

# Note (exclude exterior whitespace)
# Note: ties default to first encountered

s1 = "racecar"
s2 = "Myself and AnnabannabannA enjoy watching the noon-noontime racecars."

trimWtSpc = True

def largestPalin(string, trim=None):
    if trim == None: trim = False
    largest = ""
    for start in range(len(string)):
        for end in range(len(string)+1):
            substr = string[start:end]
            # print(substr)
            # print(isPalindrome(substr))
            if trimWtSpc: substr = substr.strip()
            if isPalindrome(substr) and len(substr) > len(largest):
                # print(substr)
                # print(isPalindrome(substr))
                largest = substr
    return largest

# print(largestPalin(s1))
# print(largestPalin(s2))

# 5) How to find the first non repeated character of a given String? (solution)

# Note: if all repeat, returns -1

s1 = "aaardvark"
s2 = "apple"
s3 = "pppppp"

def firstNonRepeatedChar(string):
    for char in string:
        if list(string).count(char) == 1: return char
    return -1

# print(firstNonRepeatedChar(s1))
# print(firstNonRepeatedChar(s2))
# print(firstNonRepeatedChar(s3))


# 6) How to count the occurrence of a given character in a String? (solution)

s1 = "aaardvark"
s2 = "xylophone"

def countOccurences(string, char):
    c = 0
    for ch in string:
        if ch == char: c += 1
    return c

# print(countOccurences(s1, "a"))
# print(countOccurences(s2, "p"))
# print(countOccurences(s2, "z"))

# 7) How to check if two String are Anagram? (solution)

s1 = "friend"
s2 = "lolz"
s3 = "eidnfr"
s4 = "trinity"
s5 = "iiyttrn"

def areAnagrams(st1, st2):
    return sorted(list(st1[:])) == sorted(list(st2[:]))

# print(areAnagrams(s1, s2))
# print(areAnagrams(s1, s3))
# print(areAnagrams(s4, s5))
# print(areAnagrams(s5, s5))


# 8) How to convert numeric String to int? (solution)

s = "123"
# print(int(s) + 2)


# 9) In an array 1-n numbers are stored, one number is missing how do you find it? (solution)

# Note: returns 0 if none missing

n = 100
missing = 15
a1 = list(range(1, n+1))
del a1[missing-1]

def findMissingNo(arr):
    return sum(range(1, n+1)) - sum(arr)

# print(findMissingNo(a1))

# 10) In an array 1-n exactly one number is duplicated how do you find it? (solution)

n = 100
duped = 26
a1 = list(range(1, n+1))
a1.insert(duped-1, duped)

def findDupedNo(arr):
    return sum(arr) - sum(range(1, n+1))

# print(findDupedNo(a1))



# 11) In an array 1-100 multiple numbers are duplicates, how do you find it? (solution)
# One trick in this programming questions is by using HashMap or Hashtable, we can store a number as key and its occurrence as value if the number is already present in Hashtable then increment its value or insert value as 1 and later on print all those numbers whose values are more than one.

n = 100
dupes = [2, 9, 78]
a1 = list(range(1, n+1))
for dupe in dupes: a1.insert(dupe-1, dupe)

def findDupedNos(arr):
    d = {}
    for n in arr:
        if n in d: print(n)
        else: d[n] = 1


# findDupedNos(a1)


# 12) Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.

a1 = [1,2,3,4,5]
a2 = [2,3,1,0,5]

def findDifferentNo(arr1, arr2):
    d = {}
    for n in arr2:
        d[n] = 1
    for n in arr1:
        if n not in d: print(n)


# findDifferentNo(a1, a2)

# 13) How do you find the second highest number in an integer array? (solution)

a1 = [1,2,3,4,5, 2, 18, 27, 100009, 10007, 100000000]

def findSecondHighest(arr):
    h = float('-inf')
    h2 = h
    for n in arr: 
        h2 = h
        if n > h: h = n
    print(h2) 

# findSecondHighest(a1)

# 14) How to find all pairs in an array of integers whose sum is equal to the given number? (solution)

a1 = [0,1,2,3,4,5,6,7,8,9,10]
s1 = 10
s2 = 8
s3 = 1
s4 = 7

def findAllPairs(arr, s):
    print("Start")
    d = set()
    for n1 in arr: 
        target = s - n1
        if target in d: print(str((n1, target)) + " Sum: " + str(s))
        else: d.add(n1)
        


# findAllPairs(a1, s1)
# findAllPairs(a1, s2)
# findAllPairs(a1, s3)
# findAllPairs(a1, s4)

# 15) How to remove duplicate elements from a list? (solution)

a1 = [0,22,10,1,2,2,2,3,4,5,5,7,6,7,8,9,10,1]

def removeDupes(arr):
    d = set()
    for i in reversed(range(len(arr))): 
        if arr[i] in d: del arr[i]
        else: d.add(arr[i])
    
    print(arr)
        


# removeDupes(a1)

# Implement a Doubly Linked List in python.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None    

    def __repr__(self):
        return repr(self.data)
    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data
    def setData(self, value):
        self.data = value
    def delete(self):
        del self.data
        if self.prev != None and self.next != None: 
            self.prev.next = self.next
            self.next.prev = self.prev
    def append(self, value):
        end = self
        while(end.next != None):
            end = end.next
        value.prev = end    
        end.next = value
    def insertAfter(self, value):
        self.next.prev = value
        value.next = self.next
        self.next = value
        value.prev = self
    def prepend(self, value):
        start = self
        while(start.prev != None): 
            start = start.prev
        value.next = start
        start.prev = value
    def insertBefore(self, value):
        self.prev.next = value
        value.prev = self.prev
        self.prev = value
        value.next = self
    def printAll(self):
        arr = [self.data]
        left = self
        right = self
        while(left.prev != None): 
            arr.insert(0, left.prev.data)
            left = left.prev
        while(right.next != None): 
            arr.append(right.next.data)
            right = right.next
        print(str(arr))
    def printSLL(self):
        right = self
        arr = [self]
        while(right.next != None): 
            arr.append(right.next)
            right = right.next
        print(arr)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

# printAll(n2)
# n2.prepend(n1)
# printAll(n2)
# n2.append(n3)
# printAll(n2)

# 14) How do you find middle element of a linked list in a single pass?

def findMiddle(strt):
    c = 0
    end = strt
    mid = strt
    while(end.next != None): 
        end = end.next
        c += 1
        if c % 2 == 0: mid = mid.next
    return mid

ll = Node(42)
n2 = Node(17)
n3 = Node(100000000000000)
n4 = Node(0)
n5 = Node(40)

# ll.printAll()
# print(findMiddle(ll))
# ll.append(n2)
# ll.append(n3)
# ll.append(n4)
# ll.printAll()
# print(findMiddle(ll))
# ll.append(n5)
# ll.printAll()
# print(findMiddle(ll))



# 15) How do you find the nth element from last in a single pass? (solution)

def findNthLast(strt, n):
    if n <= 0: return -1
    end = strt
    nthLast = strt
    for i in range(n):
        end = end.next
        if end == None: return -1
    while(end.next != None): 
        end = end.next
        nthLast = nthLast.next
    return nthLast

ll = Node(42)
n2 = Node(17)
n3 = Node(100000000000000)
n4 = Node(0)
n5 = Node(40)

ll2 = Node(0)
for i in range(1, 10):
    ll2.append(Node(i))

# ll.append(n2)
# ll.append(n3)
# ll.append(n4)
# ll.printAll()
# print(findNthLast(ll, 2))
# ll.append(n5)
# ll.printAll()
# print(findNthLast(ll, 0))
# ll.printAll()
# print(findNthLast(ll, 1))
# ll2.printAll()
# print(findNthLast(ll2, 7))

# 17) How do you reverse a singly linked list? (solution)

def reverseSLL(sll):
    end = sll
    stack = [sll]
    while(end.next != None):
        stack.append(end.next)
        end = end.next

    while(len(stack) > 0):
        end = stack.pop()
        end.next = stack[len(stack)-1] if len(stack)-1 >= 0 else None
    
ll = Node(42)
n2 = Node(17)
n3 = Node(100000000000000)
n4 = Node(0)
n5 = Node(40)
n6 = Node(-9278)

ll2 = Node(0)
end = ll2
for i in range(1, 10):
    end = Node(i)
    ll2.append(end)

# ll.append(n2)
# ll.append(n3)
# ll.append(n4)
# ll.append(n5)
# ll.append(n6)
# ll.printAll()
# reverseSLL(ll)
# ll.printAll()
# ll2.printAll()
# reverseSLL(ll2)
# end.printSLL()

# 17.1) How about a DLL?

def reverseDLL(dll):
    cur = dll
    last = None
    while(cur.next != None):
        cur.prev = cur.next
        last = cur
        cur = cur.next


ll = Node(42)
n2 = Node(17)
n3 = Node(100000000000000)
n4 = Node(0)
n5 = Node(40)
n6 = Node(-9278)

ll2 = Node(0)
for i in range(1, 10):
    ll2.append(Node(i))

# ll.append(n2)
# ll.append(n3)
# ll.append(n4)
# ll.append(n5)
# ll.append(n6)
# ll.printAll()
# reverseDLL(ll)
# ll.printAll()
ll2.printAll()
reverseDLL(ll2)
ll2.printAll()

# 18) Difference between a linked list and array data structure? (answer)

