# Kaitlyn Jarrett
# Assignment 2
# 2/21/16

# I could have used ACSII, but I figured why not do this instead.
lookup = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F',
        6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
        12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
        18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
        24: 'Y', 25: 'Z', 26: ',', 27: '.', 28: '-', 29:'_'};

ilookup = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
        'G': 6, 'H': 7, 'I':8, 'J': 9, 'K': 10, 'L': 11,
        'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
        'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
        'Y': 24, 'Z': 25, ',': 26, '.': 27, '-': 28, '_': 29};

original = raw_input('Enter the text to encode: ') #"SIU_CS-Department_is_the_best"#
original=original.upper()

key = raw_input('Enter the key: ') #"Carbondale"
k = len(key)
key=key.upper()

encoded= ""
last=0
j=0

for i in original:
    if j==k:
        key = key + encoded[last:j]
        last=j
        k = len(key)
    num= (ilookup[i]+ilookup[key[j]])%30
    char = lookup[num]
    encoded= encoded+ char
    j=j+1
print encoded
