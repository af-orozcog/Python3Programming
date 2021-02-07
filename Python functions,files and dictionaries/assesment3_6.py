"""
Create the dictionary characters that shows each character from the string sally and its frequency. 
Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
"""

sally = "sally sells sea shells by the sea shore"

characters = {}

for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1
    
chars = list(characters.keys())
best_char = chars[0]

for char in chars:
    if characters[char] > characters[best_char]:
        best_char = char