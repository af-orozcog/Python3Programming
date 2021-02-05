"""
Create a list called emotions that contains the first word of every line in emotion_words.txt.
"""
f = open("emotion_words.txt","r")

emotions = list()

for line in f:
    emotions.append(line.split()[0])