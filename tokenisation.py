import sys
from io import StringIO
import numpy as np
import matplotlib

# versions
# print("Python:", sys.version)
# print("Numpy:", np.__version__)
# print("Matplotlib:", matplotlib.__version__)

opened = open("sample.txt", "r")

try:
    # stores each paragraphs in a list including the new line character
    data = opened.readlines()
    print("before: \n", data)

    # remove new line character from list
    for d in data:
        if d == "\n":
            data.remove(d)
    # print("after: \n", data)


    individual = []
    for r in range(len(data)):
        # print(data[r])
        sentences = data[r].split() # each item from previous list (data) gets split and store in a temporary list called sentences
        for s in sentences:
            individual.append(s) # append the individual words into another list called individual


    # remove punctuation (commas and fullstops)
    for i in range(len(individual)):
        # print (individual[i][-1])
        if individual[i][-1] == "." or individual[i][-1] == ",":
            individual[i] = individual[i][:-1]

    # print final result
    for i in range(len(individual)): 
        print (individual[i])
    
finally:
    opened.close()
