"""
Create a dictionary called wrd_d 
from the string sent, so that the key is a word and the value is how many times you have seen that word.
"""

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

words = sent.split()

wrd_d = {}

for word in words:
    wrd_d[word] = wrd_d.get(word,0) + 1