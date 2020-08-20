txt = list("0123")
perms = []

# Optional complexity: for input lists with duplicate items, e.g. '022', only add distinct permutations
onlyDistinct = False

def findPerms(original, onlyAddDistinct=False, used=None, currentPerm=None, outputList=None):

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
            findPerms(original, onlyAddDistinct, usedCopy, currentPerm + [original[j]], outputList)

findPerms(txt, onlyDistinct)
for p in perms: print("".join(p))