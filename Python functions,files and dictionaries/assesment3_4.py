"""
Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
"""

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

words = str1.split()

freq_words = dict()

for word in words:
    freq_words[word] = freq_words.get(word,0) + 1