"""
Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. 
Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
"""

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

low_d = dict()

for c in p:
    low_d[c.lower()] = low_d.get(c.lower(),0) + 1