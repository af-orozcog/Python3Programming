"""
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
"""

f = open("school_prompt.txt","r")

num_lines = len(f.readlines())