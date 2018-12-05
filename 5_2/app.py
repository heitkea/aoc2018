import numpy as numpy
import re

lines = open("data.txt").read().splitlines()

input = lines[0]
newInput = ""
allChars = "abcdefghijklmnopqrstuvwxyz"
allCharRemoves = []
memory = 0

def areLettersSameAndPolar(a,b):
    if (a.lower() == b.lower()) and ( (a.isupper() and b.islower()) or (a.islower() and b.isupper()) ):
        return True
    return False

def iterateInput():
    global memory, newInput
    prevChar = ""
    if (memory < 0):
        memory = 0

    for i in range(memory,len(newInput)):
        if areLettersSameAndPolar(prevChar, newInput[i]):
            #print("Found polar match. " + prevChar + " " + newInput[i] + " at index " + str(i) + " Memory: " + str(memory))
            
            newInput = newInput[:i-1] + newInput[i+1:]
            memory = i-2
            
            return True
        prevChar = newInput[i]
    return False

def removeAllUnitsOfChar(remChar):
    global input, newInput, memory
    newInput = re.sub(remChar + "|" + remChar.upper(),"",input)
    memory = 0

    foundMatch = True
    while foundMatch == True:
        foundMatch = iterateInput()

    # print(remChar + " " + newInput)
    # print(len(newInput))

    return len(newInput)

for c in allChars:
    allCharRemoves.append([c,removeAllUnitsOfChar(c)])

allCharRemoves.sort(key=lambda tup: tup[1], reverse=True)

print(allCharRemoves)

# try 1: 10928 Too high
# try 2: 4212 Correct!
