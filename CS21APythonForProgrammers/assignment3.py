# Merges several dictionaries into one, with all the keys and values appearing in each list.

# Original Dictionaries
dict1 = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine'], 'dessert': 'ice cream'}
dict2 = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
dict3 = {'fruit': ['oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}

# Merged dictionary starts out as copy of first, skipping a run of the later loop
dictionaries = [dict2, dict3]
mergedDictionary = dict1.copy()

# Perform merge. Handles duplicate keys in the manner specified by the assignment (keys that show up once have their value as a string, while keys that show up more than once have their values in a list)

# Adds key and/or value to merged list.
# No reading from shell
# No writing to shell 
def addToMerged(key, value):
    if key not in mergedDictionary:
        mergedDictionary[key] = value 
    else:
        if isinstance(mergedDictionary[key], list):
            mergedDictionary[key].append(value)
        else:
            mergedDictionary[key] = [mergedDictionary[key]]
            mergedDictionary[key].append(value)

# Loop through all dictionary keys/values and add to merged dictionary
for dictionary in dictionaries:
    for key, value in dictionary.items():
        if isinstance(value, list):
            for item in value:
                addToMerged(key, item)
        else: 
            addToMerged(key, value)

# Prints merged dictionary.
print(mergedDictionary)

""" A RECORDING OF THE RUN
{'fruit': ['apples', 'lemons', 'oranges', 'bananas'], 'meat': ['chicken', 'hamburger'], 'vegetables': ['potatoes', 'lettuce', 'carrots'], 'drinks': ['beer', 'wine', 'apple juice', 'orange juice', 'vodka', 'milk'], 'dessert': 'ice cream'}
"""