import numpy as numpy

lines = open("data.txt").read().splitlines()

input = lines[0]
memory = 0

def areLettersSameAndPolar(a,b):
    if (a.lower() == b.lower()) and ( (a.isupper() and b.islower()) or (a.islower() and b.isupper()) ):
        return True
    return False

def iterateInput():
    global memory, input
    prevChar = ""
    if (memory < 0):
        memory = 0

    for i in range(memory,len(input)):
        if areLettersSameAndPolar(prevChar, input[i]):
            print("Found polar match. " + prevChar + " " + input[i] + " at index " + str(i) + " Memory: " + str(memory))
            
            input = input[:i-1] + input[i+1:]
            memory = i-2
            
            return True
        prevChar = input[i]
    return False



print(len(input))

foundMatch = True
while foundMatch == True:
    foundMatch = iterateInput()

print(len(input))

# try 1: 11364 Correct!