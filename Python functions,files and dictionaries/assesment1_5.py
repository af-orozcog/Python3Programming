"""
Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
"""
f = open("school_prompt.txt","r")

three = []

for line in f:
    three.append(line.split()[2])