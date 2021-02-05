"""
Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
"""
f = open("school_prompt.txt","r")

p_words = []

for line in f:
    words = line.split()
    for word in words:
        if "p" in word:
            p_words.append(word)